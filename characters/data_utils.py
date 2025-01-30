import json
import threading
from django.contrib.staticfiles import finders
from copy import deepcopy

static_data = None
static_data_lock = threading.Lock()

def format_line_breaks(text):
    return text.replace('\r\n', '<br/>').replace('\r', '<br/>').replace('\n', '<br/>')

def get_item_by_property(item_list, property_name, property_value):
    """
    Get an item from a list such that item[property_name] == property_value.
    Return None if no such item exists.
    """
    for item in item_list:
        if item[property_name] == property_value:
            return item
    return None

def get_item_by_id(item_list, item_id):
    """
    Get an item from a list such that item['id'] == item_id.
    Return None if no such item exists.
    """
    return get_item_by_property(item_list, 'id', item_id)

def denormalise_race(race, data):
    """Denormalise a race object by replacing the IDs with the corresponding entities."""
    denormalised_race = race.copy()
    denormalised_race['abilityBonuses'] = [
        { 'ability': get_item_by_id(data['abilities'], ability['ability']), 'bonus': ability['bonus']} 
        for ability in denormalised_race['abilityBonuses']]
    denormalised_race['weaponProficiencies'] = [get_item_by_id(data['items'], weapon_id) for weapon_id in denormalised_race['weaponProficiencies']]
    return denormalised_race    

def denormalise_class(class_data, data):
    """Denormalise a class object by replacing the IDs with the corresponding entities."""
    denormalised_class = class_data.copy()
    denormalised_class['proficiencies']['armor'] = [get_item_by_id(data['items'], armor_id) for armor_id in denormalised_class['proficiencies']['armor']]
    denormalised_class['proficiencies']['weapons'] = [get_item_by_id(data['items'], weapon_id) for weapon_id in denormalised_class['proficiencies']['weapons']]
    denormalised_class['proficiencies']['savingThrows'] = [get_item_by_id(data['abilities'], ability_id) for ability_id in denormalised_class['proficiencies']['savingThrows']]
    denormalised_class['proficiencies']['skills']['from'] = [get_item_by_id(data['skills'], skill_id) for skill_id in denormalised_class['proficiencies']['skills']['from']]
    denormalised_class['equipment'] = [
        { 'item': get_item_by_id(data['items'], item['item']), 'quantity': item['quantity']}
        for item in denormalised_class['equipment']]
    if denormalised_class['spellcasting']['ability'] is not None:
        denormalised_class['spellcasting']['ability'] = get_item_by_id(data['abilities'], denormalised_class['spellcasting']['ability'])
       
        denormalised_class['spellcasting']['cantrips']['from'] = [
            {**cantrip, 'description': format_line_breaks(cantrip['description'])}
            for cantrip_id in denormalised_class['spellcasting']['cantrips']['from']
            for cantrip in [get_item_by_id(data['spells'], cantrip_id)]
        ]

        denormalised_class['spellcasting']['spells']['from'] = [
            {**spell, 'description': format_line_breaks(spell['description'])}
            for spell_id in denormalised_class['spellcasting']['spells']['from']
            for spell in [get_item_by_id(data['spells'], spell_id)]
        ]
    denormalised_class['abilities'] = [
        { 'ability': get_item_by_id(data['abilities'], ability['ability']), 'value': ability['value']} 
        for ability in denormalised_class['abilities']]
    denormalised_class['primaryAbility'] = get_item_by_id(data['abilities'], denormalised_class['primaryAbility'])
    return denormalised_class

def get_static_data():
    """Get the static character creator data from the JSON file, denormalise it, and return it."""
    global static_data
    if static_data is not None:
        return deepcopy(static_data)
    
    with static_data_lock:
        if static_data is None:
            file_path = finders.find('data/characterData.json')
            with open(file_path, 'r', encoding='utf-8') as f:
                
                data = json.load(f)
                for i in range(len(data['races'])):
                    data['races'][i] = denormalise_race(data['races'][i], data)
                for i in range(len(data['classes'])):
                    data['classes'][i] = denormalise_class(data['classes'][i], data)
                static_data = data
    return deepcopy(static_data)

def validate_character_data(character_data):
    """Validate the character data."""
    data = get_static_data()
    chosen_class = get_item_by_id(data['classes'], character_data['character_class'])
    chosen_race = get_item_by_id(data['races'], character_data['race'])
    additional_skill_proficiencies = chosen_race['additionalSkillProficiencies']
    # Ensure that the character has the correct number of skills
    if len(character_data['character_class_skill_choices']) != (chosen_class['proficiencies']['skills']['choose'] + additional_skill_proficiencies):
        return False
    # Ensure that the characters skills are valid for their class
    for skill_id in character_data['character_class_skill_choices']:
        if get_item_by_id(chosen_class['proficiencies']['skills']['from'], skill_id) is None:
            return False
    # Ensure that the character has the correct number of cantrips
    if len(character_data['character_class_cantrip_choices']) != chosen_class['spellcasting']['cantrips']['choose']:
        return False
    # Ensure that the characters cantrips are valid for their class
    for cantrip_id in character_data['character_class_cantrip_choices']:
        if get_item_by_id(chosen_class['spellcasting']['cantrips']['from'], cantrip_id) is None:
            return False
    # Ensure that the character has the correct number of spells
    if len(character_data['character_class_spell_choices']) != chosen_class['spellcasting']['spells']['choose']:
        return False
    # Ensure that the characters spells are valid for their class
    for spell_id in character_data['character_class_spell_choices']:
        if get_item_by_id(chosen_class['spellcasting']['spells']['from'], spell_id) is None:
            return False
    # Ensure that the character has properly assigned ability points according to the standard array
    for score in [8, 10, 12, 13, 14, 15]:
        if get_item_by_property(character_data['ability_points'], 'value', score) is None:
            return False
    # If every test has passed, return True
    return True

