import json
from django.contrib.staticfiles import finders

data = None

def get_item_by_id(item_list, item_id):
    for item in item_list:
        if item['id'] == item_id:
            return item
    return None

def denormalise_race(race, data):
    denormalised_race = race.copy()
    


def denormalise_class_data(class_data, data):
    denormalised_data = class_data.copy()
    #denormalised_data['skills'] = [get_item_by_id(data['skills'], skill_id) for skill_id in class_data['skills']]
    #denormalised_data['cantrips'] = [get_item_by_id(data['spells'], cantrip_id) for cantrip_id in class_data['cantrips']]
    #denormalised_data['spells'] = [get_item_by_id(data['spells'], spell_id) for spell_id in class_data['spells']]
    return denormalised_data


file_path = finders.find('data/characterData.json')
#print("File path is: ", file_path)

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

#print(data)


def normalise_character_data(character_data):
    pass
    #file_path = finders.find('data/characterData.json')
    #print("File path is: ", file_path)
    #with open(file_path, 'r', encoding='utf-8') as f:
    #    data = json.load(f)
    #    print("Data is: ", data)


def validate_character_data(character_data):
    pass

