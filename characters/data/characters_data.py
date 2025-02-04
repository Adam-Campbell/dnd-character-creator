import json

users_data_list = [
    {
        'username': 'AdventurerAlice',
        'password': 'password1',
        'bio': 'A passionate gamer and story-teller who loves creating epic characters and thrilling adventures.',
    },
    {
        'username': 'dungeonmasterdave',
        'password': 'password2',
        'bio': 'Experienced dungeon master with a knack for weaving intricate plots and challenging encounters.',
    },
    {
        'username': 'ElfEnthusiast',
        'password': 'password3',
        'bio': 'Enthusiastic about all things elf-related, from lore to character creation, and loves role-playing as nimble archers.',
    },
    {
        'username': 'battlemagebobby',
        'password': 'password4',
        'bio': 'A fan of magical combat and strategy games, constantly seeking the perfect blend of might and magic.',
    },
    {
        'username': 'HeroicHelen',
        'password': 'password5',
        'bio': 'Loves diving into heroic tales and creating characters with rich backstories and unique abilities.',
    },
]


race_ids = {
    'Dwarf': '095914ea-d0a5-41dd-a003-6b5d4558a3ad',
    'Elf': '576c1e3a-8464-4c1a-bbe7-3dde6813bbd3',
    'Halfling': 'bf3b0c49-80cc-4258-85a0-3974f656469a',
    'Human': '4725316c-cfc5-44a2-a69f-563088dec352',
    'Half-Elf': 'ec1f0336-fb41-4ac8-b1f3-2a574ddb1bd5',
    'Tiefling': '8b5c75dd-3d4f-41b4-a7c2-ec516f02256e',
}

class_ids = {
    'Barbarian': '44f84547-8935-4ab4-bd29-fb60d0000d04',
    'Bard': 'ea6fbdc2-82c7-44d7-b065-bd70e136ccc7',
    'Cleric': '17d2bd00-57b7-4756-b14e-43bf1f102585',
    'Fighter': 'e72b02b5-a7d0-4b1b-860f-7c965ea5e18c',
    'Rogue': '32ea43f0-8f6f-4ce4-829c-f58955a758d1',
    'Wizard': 'ef560074-395d-4e42-b5ac-5ad9d3342271',
}

def format_ability_points(str, dex, con, int, wis, cha):
    return [
        {"id": "0caab33e-f424-4a44-94cd-0c6951e5bdfe", "value": str}, 
        {"id": "fd107c7f-4536-4b36-bf43-e49d92a3c4c2", "value": dex}, 
        {"id": "b9b14f85-78db-49ea-b07b-b8bdd7a40046", "value": con}, 
        {"id": "44fbcb3c-d548-4a3c-aa85-4c55e05aabed", "value": int}, 
        {"id": "468b3218-340b-4263-9450-dc72e6750f16", "value": wis}, 
        {"id": "b15c2aa9-87e7-408d-89a7-3bbd64d981a9", "value": cha}
    ]



characters_data_list = [
    {
        'race': race_ids['Dwarf'],
        'character_class': class_ids['Fighter'],
        'character_class_skill_choices': [
            "0cf988cb-ed38-40f8-948f-91b679cf502c",
            "57b45a74-aacb-4ea7-9d5d-8219b8f15851"
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(15, 13, 14, 12, 10, 8),
        'name':  'Thrain "Ironheart" Stonefist',
        'age': 125,
        'gender': 'Male',
        'alignment': 'Lawful Good',
        'background': "Born in the mountain stronghold of Kazad'Bral, Thrain was raised in a family of esteemed warriors. From a young age, he trained in the art of war, wielding an axe before he could even grow a beard. His father, a decorated general, expected nothing less than perfection. Thrain fought in skirmishes against goblin raiders, proving himself in battle. However, after a tragic ambush claimed his father’s life, Thrain took an oath to defend those who could not defend themselves. Leaving his home, he now travels the land, seeking to uphold honour and protect the innocent.",
        'traits': [
            'Disciplined and honour-bound',
            'Speaks in a deep, gravelly voice, always to the point',
            'Has a soft spot for children and the elderly'
        ],
        'ideals': [
            'Honour is everything',
            'Strength must serve the weak'
        ],
        'bonds': [
            "His father's old war axe, which he carries at all times",
            'A promise made to a dying comrade to keep his family safe'
        ],
        'flaws': [
            'Struggles to forgive himself for past failures',
            'Slow to trust outsiders',
            'Can be stubborn to a fault'
        ],
        'height': '4\'10"',
        'build': 'Stocky and broad-shouldered',
        'skin_tone': 'Weathered tan',
        'hair_color': 'Dark brown',
        'hair_style': 'Thick and well-groomed',
        'hair_length': 'Medium',
        'hair_type': 'Wavy',
        'facial_hair_style': 'Full beard',
        'facial_hair_length': 'Long',
        'eye_color': 'Dark brown',
        'eye_shape': 'Hooded',
        'distinguishing_features': 'A long scar running from his forehead to his cheek, received in battle',
        'clothing_style': 'Sturdy, practical dwarven armour with fur-lined cloak',
        'clothing_colors': 'Earthy browns and deep greys',
        'clothing_accessories': 'A thick leather belt with a family crest buckle',
    },
    {
        'race': race_ids['Elf'],
        'character_class': class_ids['Bard'],
        'character_class_skill_choices': [
            "2d27709a-bc52-422e-9268-0f9f3967c5f9",
            "3bbcebbe-8e83-49af-97e0-66648d020ccb",
            "affa7db3-34db-4f19-aca3-afae012f47b4"
        ],
        'character_class_cantrip_choices': [
            "8a2a3ffd-c383-460a-8db7-ea0abe72c419",
            "66e4a647-cf9f-442a-9c31-db2ae0483cc4",
        ],
        'character_class_spell_choices': [
            "ad6c7f3a-6770-497d-91bd-ae164f7cca4b", 
            "52b6c000-7810-4857-988b-81db81185ede",
            "e5c90b9e-9590-4050-9dc7-40f14e2c6ae1",
            "fb37362f-1985-474e-a399-7401b80ab5d7"
        ],
        'ability_points': format_ability_points(8, 14, 12, 13, 10, 15),
        'name': 'Lirien Moonwhisper',
        'age': 212,
        'gender': 'Female',
        'alignment': 'Chaotic Good',
        'background': 'Lirien was raised among the highborn elves of Silverymist but found court life suffocating. Instead of learning courtly etiquette, she snuck away to listen to minstrels and street performers. When her family attempted to arrange a marriage, she vanished, trading the life of nobility for one of adventure. With her silver tongue and quick wit, she has travelled from bustling cities to forgotten ruins, collecting stories and songs along the way. Though she enjoys the thrill of the unknown, there’s a part of her that still wonders if she can ever go home.',
        'traits': [
            'A natural flirt who enjoys teasing people',
            'Speaks in an almost melodic tone, as if always performing',
            'Can play almost any instrument with ease'
        ],
        'ideals': [
            'Life is a story waiting to be told',
            'Rules are suggestions, not laws'
        ],
        'bonds': [
            'Carries a locket with a tiny portrait of her estranged sister',
            'Her enchanted lute, a gift from a travelling musician she once loved'
        ],
        'flaws': [
            'Struggles with commitment, always on the move',
            'Overconfident in her own charm',
            'Has a tendency to embellish stories, sometimes to her own detriment'
        ],
        'height': '5\'7"',
        'build': 'Slim and elegant',
        'skin_tone': 'Fair with a slight silver sheen',
        'hair_color': 'Platinum blonde',
        'hair_style': 'Long and straight, often tucked behind her ears',
        'hair_length': 'Long',
        'hair_type': 'Straight',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Ice blue',
        'eye_shape': 'Almond',
        'distinguishing_features': ' A tattoo of a crescent moon on her wrist',
        'clothing_style': 'Flowing silk tunics and embroidered vests',
        'clothing_colors': 'Deep blues, silvers, and purples',
        'clothing_accessories': 'A silver ring that hums with magic when she sings',
    },
    {
        'race': race_ids['Halfling'],
        'character_class': class_ids['Rogue'],
        'character_class_skill_choices': [
            "f0282ac7-16a8-42c4-a50f-4336db5c0162",
            "5fec3a3b-806d-47c5-9101-2fb77832ec18",
            "c0570ecd-b0f1-4cdf-b71a-a558cdef866d",
            "032f782b-2b99-4da4-8fcd-8dae8a207d7d"
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(10, 15, 14, 12, 8, 13),
        'name': 'Rhyssa Thornbrook',
        'age': 35,
        'gender': 'Female',
        'alignment': 'True Neutral',
        'background': "Rhyssa grew up in the slums of a bustling city, learning to survive through cunning rather than strength. Orphaned at a young age, she became a pickpocket and street performer to get by. Eventually, she caught the eye of a thieves' guild and was trained in the art of burglary and deception. Though she has no love for the law, she isn’t without her own morals—she steals from the rich, the corrupt, and those who can afford to lose a few coins. She dreams of one day pulling off the greatest heist in history and retiring to a life of comfort.",
        'traits': [
            'Quick-witted and always ready with a sarcastic remark',
            'Enjoys gambling, especially when the odds are against her',
            'Has a habit of flipping a coin when making decisions',
        ],
        'ideals': [
            'Fortune favours the bold',
            'The world isn’t fair—so why should I play fair?',
        ],
        'bonds': [
            'Still keeps a lucky coin given to her by an old friend',
            'Owes a life debt to a former partner who saved her from an ambush',
        ],
        'flaws': [
            'Can be reckless and overconfident',
            'Struggles to let people get too close',
            'Has a soft spot for children in need, which sometimes compromises her work'
        ],
        'height': '3\'1"',
        'build': 'Petite but athletic',
        'skin_tone': 'Warm caramel',
        'hair_color': 'Chestnut brown',
        'hair_style': 'Messy and often tucked under a hood',
        'hair_length': 'Short',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Green',
        'eye_shape': 'Round',
        'distinguishing_features': 'A small scar on her left cheek from a botched job',
        'clothing_style': 'Dark leather armour, perfect for blending into shadows',
        'clothing_colors': 'Blacks, greys, and dark blues',
        'clothing_accessories': 'A belt full of hidden pockets and lockpicks',
    },
]


fields = [
   {
        'race': '',
        'character_class': '',
        'character_class_skill_choices': [],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': [],
        'name': '',
        'age': 0,
        'gender': '',
        'alignment': '',
        'background': '',
        'traits': [],
        'ideals': [],
        'bonds': [],
        'flaws': [],
        'height': '',
        'build': '',
        'skin_tone': '',
        'hair_color': '',
        'hair_style': '',
        'hair_length': '',
        'hair_type': '',
        'facial_hair_style': '',
        'facial_hair_length': '',
        'eye_color': '',
        'eye_shape': '',
        'distinguishing_features': '',
        'clothing_style': '',
        'clothing_colors': '',
        'clothing_accessories': '',
    }, 
]


