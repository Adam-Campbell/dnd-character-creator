from django import forms
from .models import Character
from .data_utils import get_static_data, get_item_by_id
import uuid

def get_item_by_uuid(item_list, uuid_object):
    for item in item_list:
        uuid_str = item.get('id')
        if uuid_str is not None:
            if uuid.UUID(uuid_str) == uuid_object:
                return item
    return None

class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = [
            'race', 'character_class',  'character_class_skill_choices',
            'character_class_cantrip_choices', 'character_class_spell_choices', 'ability_points',
            'name', 'age', 'gender', 'alignment', 'background', 'traits', 'ideals', 'bonds', 'flaws',
            'height', 'build', 'skin_tone', 'hair_color', 'hair_style', 'hair_length', 'hair_type',
            'facial_hair_style', 'facial_hair_length', 'eye_color', 'eye_shape', 'distinguishing_features',
            'clothing_style', 'clothing_colors', 'clothing_accessories', 'image'
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        # Django forms set empty lists to None for JSONField fields, but we want to keep them as empty lists,
        # so we need to check for None and set them to empty lists if they are None
        jsonFields = ['character_class_skill_choices', 'character_class_cantrip_choices', 
                      'character_class_spell_choices', 'ability_points', 'traits', 
                      'ideals', 'bonds', 'flaws'
        ]
        for field in jsonFields:
            data = cleaned_data.get(field, [])
            if data is None:
                cleaned_data[field] = []
        
        static_data = get_static_data()
        race_data = get_item_by_uuid(static_data['races'], cleaned_data['race'])
        character_class_data = get_item_by_uuid(static_data['classes'], cleaned_data['character_class'])
        # Check that character_class_skill_choices has the correct number of skills, and that they
        # are valid for the chosen class
        total_skill_choices = character_class_data['proficiencies']['skills']['choose'] + race_data['additionalSkillProficiencies']
        if len(cleaned_data['character_class_skill_choices']) != total_skill_choices:
            self.add_error('character_class_skill_choices', "You must choose the correct number of skills.")
        for skill_id in cleaned_data['character_class_skill_choices']:
            skill_obj = get_item_by_id(character_class_data['proficiencies']['skills']['from'], skill_id)
            if skill_obj is None:
                self.add_error('character_class_skill_choices', "You must choose valid skills.")
        # Check that character_class_cantrip_choices has the correct number of cantrips, and that they
        # are valid for the chosen class
        if len(cleaned_data['character_class_cantrip_choices']) != character_class_data['spellcasting']['cantrips']['choose']:
            self.add_error('character_class_cantrip_choices', "You must choose the correct number of cantrips.")
        for cantrip_id in cleaned_data['character_class_cantrip_choices']:
            cantrip_obj = get_item_by_id(character_class_data['spellcasting']['cantrips']['from'], cantrip_id)
            if cantrip_obj is None:
                self.add_error('character_class_cantrip_choices', "You must choose valid cantrips.")
        # Check that character_class_spell_choices has the correct number of spells, and that they
        # are valid for the chosen class
        if len(cleaned_data['character_class_spell_choices']) != character_class_data['spellcasting']['spells']['choose']:
            self.add_error('character_class_spell_choices', "You must choose the correct number of spells.")
        for spell_id in cleaned_data['character_class_spell_choices']:
            spell_obj = get_item_by_id(character_class_data['spellcasting']['spells']['from'], spell_id)
            if spell_obj is None:
                self.add_error('character_class_spell_choices', "You must choose valid spells.")
        # Check that the character has properly assigned ability points according to the standard array
        standard_array = [15, 14, 13, 12, 10, 8]
        for score in standard_array:
            if score not in [ability['value'] for ability in cleaned_data['ability_points']]:
                self.add_error('ability_points', "You must assign ability points according to the standard array.")
        # Check that facial_hair_length is an empty string if facial_hair_style is 'None' or 'Stubble'
        if cleaned_data['facial_hair_style'] in ['None', 'Stubble'] and cleaned_data['facial_hair_length'] != '':
            self.add_error('facial_hair_length', "You must leave facial hair length empty if facial hair style is 'None' or 'Stubble'.")
        return cleaned_data
