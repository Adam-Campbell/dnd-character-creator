

/**
 * Factory function for creating a new, empty character object
 * @returns 
 */
export function getEmptyCharacter() {
    return {
        race: "095914ea-d0a5-41dd-a003-6b5d4558a3ad",
        class: "44f84547-8935-4ab4-bd29-fb60d0000d04",
        classSkillChoices: [],
        classCantripChoices: [],
        classSpellChoices: [],
        abilityPoints: [
            { id: "0caab33e-f424-4a44-94cd-0c6951e5bdfe", value: '--' },
            { id: "fd107c7f-4536-4b36-bf43-e49d92a3c4c2", value: '--' },
            { id: "b9b14f85-78db-49ea-b07b-b8bdd7a40046", value: '--' },
            { id: "44fbcb3c-d548-4a3c-aa85-4c55e05aabed", value: '--' },
            { id: "468b3218-340b-4263-9450-dc72e6750f16", value: '--' },
            { id: "b15c2aa9-87e7-408d-89a7-3bbd64d981a9", value: '--' },
        ],
        name: "",
        age: null,
        gender: "",
        alignment: "True Neutral",
        background: "",
        traits: [],
        ideals: [],
        bonds: [],
        flaws: [],
        height: "",
        build: "",
        skinTone: "",
        hairColor: "",
        hairStyle: "",
        hairLength: "Medium",
        hairType: "Straight",
        facialHairStyle: "None",
        facialHairLength: "",
        eyeColor: "",
        eyeShape: "Almond",
        distinguishingFeatures: "",
        clothingStyle: "",
        clothingColors: "",
        clothingAccessories: "",
        imageUrl: ""
    };
}

const namingConventionMap = {
    id: 'id',
    race: 'race',
    name: 'name',
    age: 'age',
    gender: 'gender',
    alignment: 'alignment',
    background: 'background',
    traits: 'traits',
    ideals: 'ideals',
    bonds: 'bonds',
    flaws: 'flaws',
    height: 'height',
    build: 'build',
    class: 'character_class',
    character_class: 'class',
    classSkillChoices: 'character_class_skill_choices',
    character_class_skill_choices: 'classSkillChoices',
    classCantripChoices: 'character_class_cantrip_choices',
    character_class_cantrip_choices: 'classCantripChoices',
    classSpellChoices: 'character_class_spell_choices',
    character_class_spell_choices: 'classSpellChoices',
    abilityPoints: 'ability_points',
    ability_points: 'abilityPoints',
    skinTone: 'skin_tone',
    skin_tone: 'skinTone',
    hairColor: 'hair_color',
    hair_color: 'hairColor',
    hairStyle: 'hair_style',
    hair_style: 'hairStyle',
    hairLength: 'hair_length',
    hair_length: 'hairLength',
    hairType: 'hair_type',
    hair_type: 'hairType',
    facialHairStyle: 'facial_hair_style',
    facial_hair_style: 'facialHairStyle',
    facialHairLength: 'facial_hair_length',
    facial_hair_length: 'facialHairLength',
    eyeColor: 'eye_color',
    eye_color: 'eyeColor',
    eyeShape: 'eye_shape',
    eye_shape: 'eyeShape',
    distinguishingFeatures: 'distinguishing_features',
    distinguishing_features: 'distinguishingFeatures',
    clothingStyle: 'clothing_style',
    clothing_style: 'clothingStyle',
    clothingColors: 'clothing_colors',
    clothing_colors: 'clothingColors',
    clothingAccessories: 'clothing_accessories',
    clothing_accessories: 'clothingAccessories',
    imageUrl: 'image_url',
    image_url: 'imageUrl'
}

export function switchObjectNamingConventions(obj) {
    const newObj = {};
    for (const key in obj) {
        if (Object.hasOwnProperty.call(obj, key) && namingConventionMap[key]) {
            const newKey = namingConventionMap[key];
            newObj[newKey] = obj[key];
        }
    }
    return newObj;
}


/**
 * Denormalises a single class object, replacing id references with actual entities.
 * Mutates the class object rather than creating a new one.
 * @param {*} cls 
 * @param {*} data 
 */
function denormaliseClass(cls, data) {
    // Equipment needs to have its shape changed
    cls.equipment = cls.equipment.map(e => {
        const item = data.items.find(i => i.id === e.item);
        return {
            item: item,
            quantity: e.quantity
        }
    });
    // Abilities need to have their shape changed
    cls.abilities = cls.abilities.map(a => {
        const ability = data.abilities.find(i => i.id === a.ability);
        return {
            ability: ability,
            value: a.value
        }
    });
    cls.primaryAbility = data.abilities.find(a => a.id === cls.primaryAbility);
    // Proficiencies can just be replaced as-is
    cls.proficiencies.armor = cls.proficiencies.armor.map(a => data.items.find(i => i.id === a));
    cls.proficiencies.weapons = cls.proficiencies.weapons.map(w => data.items.find(i => i.id === w));
    cls.proficiencies.savingThrows = cls.proficiencies.savingThrows.map(s => data.abilities.find(i => i.id === s));
    cls.proficiencies.skills.from = cls.proficiencies.skills.from.map(s => data.skills.find(i => i.id === s));
    // Spellcasting can be replaced as-is, but only if the class is a caster class.
    if (cls.spellcasting.ability !== null) {
        cls.spellcasting.ability = data.abilities.find(a => a.id === cls.spellcasting.ability);
        cls.spellcasting.cantrips.from = cls.spellcasting.cantrips.from.map(id => data.spells.find(c => c.id === id));
        cls.spellcasting.spells.from = cls.spellcasting.spells.from.map(id => data.spells.find(s => s.id === id));
    }
}

/**
 * Denormalises a single race, replacing id references with actual entities.
 * Mutates the race object rather than creating a new one.
 * @param {*} race 
 * @param {*} data 
 */
function denormaliseRace(race, data) {
    // We need to change the shape of ability bonuses
    race.abilityBonuses = race.abilityBonuses.map(abilityBonus => {
        const ability = data.abilities.find(a => a.id === abilityBonus.ability);
        return {
            ability: ability,
            bonus: abilityBonus.bonus
        }
    });
    // Weapon proficiencies can be replaced as-is
    race.weaponProficiencies = race.weaponProficiencies.map(w => data.items.find(i => i.id === w));
}

/**
 * Denormalises the data. Mutates the data object rather than creating a new one.
 * a new one.
 * @param {*} data 
 * @returns 
 */
export function denormaliseData(data) {
    //combineItems(data);
    data.classes.forEach(cls => denormaliseClass(cls, data));
    data.races.forEach(race => denormaliseRace(race, data));
    // return the data object just for flexibility
    return data;
}

/**
 * Fetches the static data JSON file, parses it and denormalises it.
 * @returns 
 */
export async function fetchStaticData() {
    try {
        const response = await fetch('/static/data/characterData.json');
        const staticData = await response.json();
        denormaliseData(staticData);
        return staticData;
    } catch (error) {
        console.error('Error fetching JSON:', error);
    }
}

/**
 * Retrieves the value of a cookie by name.
 * @param {*} name 
 * @returns 
 */
export function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}