import json
import threading
from copy import deepcopy
from django.contrib.staticfiles import finders
from cloudinary.utils import cloudinary_url


def get_image_url(public_id, format="webp", width=500, height=500):
    """
    Take a public ID of an image stored in Cloudinary and returns the URL of
    a transformed version of the image with the specified format, width, and
    height. The image is also served over HTTPS.
    """
    url, options = cloudinary_url(
        public_id,
        format=format,
        width=width,
        height=height,
        secure=True
    )
    return url


static_data = None
static_data_lock = threading.Lock()


def format_line_breaks(text):
    """Replace line breaks in the text with HTML line breaks."""
    return text.replace(
        '\r\n', '<br/>'
    ).replace('\r', '<br/>').replace('\n', '<br/>')


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
    """
    Denormalise a race object by replacing the IDs with the corresponding
    entities.
    """
    denormalised_race = race.copy()

    denormalised_race['abilityBonuses'] = [
        {
            'ability': get_item_by_id(data['abilities'], ability['ability']),
            'bonus': ability['bonus']
        }
        for ability in denormalised_race['abilityBonuses']]

    denormalised_race['weaponProficiencies'] = [
        get_item_by_id(data['items'], weapon_id)
        for weapon_id in denormalised_race['weaponProficiencies']
    ]

    return denormalised_race


def denormalise_class(class_data, data):
    """
    Denormalise a class object by replacing the IDs with the corresponding
    entities.
    """
    denormalised_class = class_data.copy()

    denormalised_class['proficiencies']['armor'] = [
        get_item_by_id(data['items'], armor_id)
        for armor_id in denormalised_class['proficiencies']['armor']
    ]

    denormalised_class['proficiencies']['weapons'] = [
        get_item_by_id(data['items'], weapon_id)
        for weapon_id in denormalised_class['proficiencies']['weapons']
    ]

    denormalised_class['proficiencies']['savingThrows'] = [
        get_item_by_id(data['abilities'], ability_id)
        for ability_id in denormalised_class['proficiencies']['savingThrows']
    ]

    denormalised_class['proficiencies']['skills']['from'] = [
        get_item_by_id(data['skills'], skill_id)
        for skill_id in denormalised_class['proficiencies']['skills']['from']
    ]

    denormalised_class['equipment'] = [
        {
            'item': get_item_by_id(data['items'], item['item']),
            'quantity': item['quantity']
        }
        for item in denormalised_class['equipment']]

    if denormalised_class['spellcasting']['ability'] is not None:
        denormalised_class['spellcasting']['ability'] = get_item_by_id(
            data['abilities'],
            denormalised_class['spellcasting']['ability']
        )

        denormalised_class['spellcasting']['cantrips']['from'] = [
            {
                **cantrip,
                'description': format_line_breaks(cantrip['description'])
            }
            for cantrip_id in (
                denormalised_class['spellcasting']['cantrips']['from']
            )
            for cantrip in [get_item_by_id(data['spells'], cantrip_id)]
        ]

        denormalised_class['spellcasting']['spells']['from'] = [
            {
                **spell,
                'description': format_line_breaks(spell['description'])
            }
            for spell_id in (
                denormalised_class['spellcasting']['spells']['from']
            )
            for spell in [get_item_by_id(data['spells'], spell_id)]
        ]

    denormalised_class['abilities'] = [
        {
            'ability': get_item_by_id(data['abilities'], ability['ability']),
            'value': ability['value']
        }
        for ability in denormalised_class['abilities']]

    denormalised_class['primaryAbility'] = get_item_by_id(
        data['abilities'], denormalised_class['primaryAbility']
    )

    return denormalised_class


def get_static_data():
    """Get the static character creator data from the JSON file, denormalise
    it, and return it.
    """
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
                    data['classes'][i] = denormalise_class(
                        data['classes'][i], data
                    )
                static_data = data
    return deepcopy(static_data)
