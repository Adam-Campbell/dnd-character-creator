import json

users_data_list = [
    {
        'username': 'AdventurerAlice',
        'password': 'password1',
        'bio': 'A passionate gamer and story-teller who loves creating epic characters and thrilling adventures.',
        'image': 'adventuring-alice_goc4ha'
    },
    {
        'username': 'dungeonmasterdave',
        'password': 'password2',
        'bio': 'Experienced dungeon master with a knack for weaving intricate plots and challenging encounters.',
        'image': 'dungeonmaster-dave_vy1vfq'
    },
    {
        'username': 'ElfEnthusiast',
        'password': 'password3',
        'bio': 'Enthusiastic about all things elf-related, from lore to character creation, and loves role-playing as nimble archers.',
        'image': 'elf-enthusiast_qcfiq1'
    },
    {
        'username': 'battlemagebobby',
        'password': 'password4',
        'bio': 'A fan of magical combat and strategy games, constantly seeking the perfect blend of might and magic.',
        'image': 'battlemage-bobby_mysfnp'
    },
    {
        'username': 'HeroicHelen',
        'password': 'password5',
        'bio': 'Loves diving into heroic tales and creating characters with rich backstories and unique abilities.',
        'image': 'heroic-helen_clrsfl'
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
        'facial_hair_style': 'Full Beard',
        'facial_hair_length': 'Long',
        'eye_color': 'Dark brown',
        'eye_shape': 'Hooded',
        'distinguishing_features': 'A long scar running from his forehead to his cheek, received in battle',
        'clothing_style': 'Sturdy, practical dwarven armour with fur-lined cloak',
        'clothing_colors': 'Earthy browns and deep greys',
        'clothing_accessories': 'A thick leather belt with a family crest buckle',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738944749/eiep41owpyuixoqvdqgh.png"
        'image': "eiep41owpyuixoqvdqgh"
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
        'distinguishing_features': 'A tattoo of a crescent moon on her wrist',
        'clothing_style': 'Flowing silk tunics and embroidered vests',
        'clothing_colors': 'Deep blues, silvers, and purples',
        'clothing_accessories': 'A silver ring that hums with magic when she sings',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738944752/c6yz49xdfprbodlq5ld9.png"
        'image': "c6yz49xdfprbodlq5ld9"
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
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738944744/pex1odq7celrtmhm8ln8.png"
        'image': "pex1odq7celrtmhm8ln8"
    },
    {
        'race': race_ids['Tiefling'],
        'character_class': class_ids['Wizard'],
        'character_class_skill_choices': [
            "d8eb6094-2655-4fdd-bfb4-ed01163c4cf5",
            "f0e83eb0-d3a7-40ee-b1a5-ea146b4dd094"
        ],
        'character_class_cantrip_choices': [
            "b692b950-1530-4112-81a3-710f723d9612",
            "1954b842-4004-4aa7-84bd-e8eb30fe1744",
            "6ed84f5f-d26a-426e-a1e3-99ac71dcfb47"
        ],
        'character_class_spell_choices': [
            "61958401-59a0-4bde-bd12-d9ca419ae4db", 
            "52b6c000-7810-4857-988b-81db81185ede",
            "79d4e2a3-96c2-499f-b0dd-154fadb132cf", 
            "02504055-b348-42af-aa50-757ccb4200da",
            "8d25c369-8660-47ba-a67d-c54a1e56ff2f", 
            "7dab1502-53f2-4020-9a31-cb83d36582cd",
        ],
        'ability_points': format_ability_points(8,14,12,15,13,10),
        'name': 'Varek "Ashen" Kalaris',
        'age': 32,
        'gender': 'Male',
        'alignment': 'Neutral Good',
        'background': "Born in the backstreets of a sprawling metropolis, Varek's infernal heritage marked him for hardship from birth. Orphaned at a young age, he survived through wits and sheer determination. One fateful night, he attempted to pickpocket an old man, only to discover he was a reclusive wizard. Rather than punishing him, the wizard took him in as an apprentice, seeing potential in the boy’s sharp mind. Years later, after mastering the arcane arts, Varek now seeks to unravel the mysteries of magic, always searching for lost knowledge that could reshape the world—for better or worse.",
        'traits': [
            'Speaks with an almost eerie calm, even in chaos',
            'Always taking notes in a weathered old book',
            'Has an obsession with fire-based spells'
        ],
        'ideals': [
            'Knowledge is the key to power',
            'Magic should be for all, not just the elite'
        ],
        'bonds': [
            'Wears a ring that belonged to his late mentor',
            'His spellbook, filled with both arcane knowledge and personal musings'
        ],
        'flaws': [
            'Distrustful of organised institutions, especially magical ones',
            'Can be reckless in the pursuit of knowledge',
            'Struggles with social norms, sometimes coming off as distant or detached'
        ],
        'height': '5\'11"',
        'build': 'Lean and wiry',
        'skin_tone': 'Ash-grey',
        'hair_color': 'Jet black',
        'hair_style': 'Tied back into a loose ponytail',
        'hair_length': 'Long',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Glowing amber',
        'eye_shape': 'Upturned',
        'distinguishing_features': 'Black, curling horns and faint, ember-like veins on his hands',
        'clothing_style': 'Flowing dark robes with silver arcane symbols',
        'clothing_colors': 'Deep crimson and midnight blue',
        'clothing_accessories': 'A leather-bound spellbook chained to his belt',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738944211/brazyorvcuhi571c3u5u.png"
        'image': "brazyorvcuhi571c3u5u"
    },
    {
        'race': race_ids['Half-Elf'],
        'character_class': class_ids['Barbarian'],
        'character_class_skill_choices': [
            "46323de2-37a8-4b4e-9b63-63bec924f21c",
            "fc38c64c-bc06-4fd1-b38e-3912d517635d",
            "f0282ac7-16a8-42c4-a50f-4336db5c0162"
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(15,14,13,10,12,8),
        'name': 'Eryndel "The Red Hawk" Vaeloria',
        'age': 38,
        'gender': 'Female',
        'alignment': 'Chaotic Neutral',
        'background': """Born to an elven diplomat and a human mercenary, Eryndel never fit in anywhere. When diplomacy failed her family, war found her instead. Captured by raiders as a child, she fought her way out, forging a new life on the high seas as a feared pirate captain. Known as "The Red Hawk" for her wild fighting style and fiery hair, she has pillaged noble vessels and warships alike. Now, with a price on her head and an old enemy hunting her, she’s looking for new allies and an even greater thrill.""",
        'traits': [
            'Laughs in the face of danger',
            'Speaks bluntly and with little regard for titles or rank',
            'Never backs down from a challenge'
        ],
        'ideals': [
            'Freedom is the only true law',
            'No man should be chained—by rulers, by fate, or by fear'
        ],
        'bonds': [
            'Her old ship’s flag, which she keeps as a reminder of her lost crew',
            'An enchanted cutlass stolen from a navy admiral'
        ],
        'flaws': [
            'Quick to anger and slow to forgive',
            'Overindulgent—drinks and gambles too much',
            'Struggles with authority and refuses to take orders'
        ],
        'height': '5\'9"',
        'build': 'Athletic and muscular',
        'skin_tone': 'Sun-kissed bronze',
        'hair_color': 'Fiery red',
        'hair_style': 'Wild and windswept',
        'hair_length': 'Medium',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Emerald green',
        'eye_shape': 'Hooded',
        'distinguishing_features': 'A jagged scar running across her nose and cheek',
        'clothing_style': 'Rugged pirate garb with a long coat and high boots',
        'clothing_colors': 'Deep crimson and black',
        'clothing_accessories': 'A shark tooth necklace and a golden hoop earring',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738944214/yfqjyxl3gsxyrllgl5rm.png"
        'image': "yfqjyxl3gsxyrllgl5rm"
    },
    {
        'race': race_ids['Human'],
        'character_class': class_ids['Cleric'],
        'character_class_skill_choices': [
            "5fec3a3b-806d-47c5-9101-2fb77832ec18",
            "540937ab-6c67-4c5f-9102-c8b180729a8e"
        ],
        'character_class_cantrip_choices': [
            "87b8c250-f2cc-4920-9b43-0046a8b34e55", 
            "d535e9f5-9ae8-46d0-8b55-ab85b9689729", 
            "a9db1992-544e-4fe9-8306-704bf0bea062",
        ],
        'character_class_spell_choices': [
            "eedc57b0-5c91-4254-a8d2-d93cb54b2ad8", 
            "07e69325-723f-45e1-a632-8a747d835728",
            "53541979-b39b-46c7-82f5-125820bab4a4",
        ],
        'ability_points': format_ability_points(12,8,14,13,15,10),
        'name': 'Father Tomas Blackwell',
        'age': 46,
        'gender': 'Male',
        'alignment': 'Lawful Neutral',
        'background': """Once a soldier, Tomas fought in brutal wars that left his soul scarred. Seeking redemption, he turned to the gods, dedicating his life to healing instead of harming. Now a wandering cleric, he travels the land tending to the wounded, both in body and spirit. Though his faith is strong, he struggles with doubts, haunted by the horrors of war. He believes in order and discipline but wrestles with the question of whether all laws are just.""",
        'traits': [
            'Always carries a worn prayer book, even in battle',
            'Never raises his voice, even when angered',
            'Offers kindness to strangers, but remains wary of deception'
        ],
        'ideals': [
            'Even the darkest soul can find the light',
            'Order and structure keep the world from falling apart'
        ],
        'bonds': [
            'The holy symbol of his deity, given to him by a fallen friend',
            'His old battle-worn sword, which he rarely uses but cannot abandon'
        ],
        'flaws': [
            'Haunted by past sins and struggles to forgive himself',
            'Can be overly rigid, sometimes following rules too strictly',
            'Distrusts magic that does not come from the gods'
        ],
        'height': '5\'11"',
        'build': 'Broad and strong, but slightly weathered',
        'skin_tone': 'Pale with hints of grey from stress and age',
        'hair_color': 'Dark brown with streaks of grey',
        'hair_style': 'Neatly combed back',
        'hair_length': 'Short',
        'hair_type': 'Straight',
        'facial_hair_style': 'Goatee',
        'facial_hair_length': 'Medium',
        'eye_color': 'Steel grey',
        'eye_shape': 'Downturned',
        'distinguishing_features': 'A faded burn scar on his left hand',
        'clothing_style': 'Simple, well-maintained priestly robes with chainmail underneath',
        'clothing_colors': 'White and gold, with dark blue accents',
        'clothing_accessories': 'A rosary of carved bone beads',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738944209/uc8wqdhanl60wxk3upwr.png"
        'image': "uc8wqdhanl60wxk3upwr"
    },
    {
        'race': race_ids['Half-Elf'],
        'character_class': class_ids['Rogue'],
        'character_class_skill_choices': [
            "fc38c64c-bc06-4fd1-b38e-3912d517635d",
            "3bbcebbe-8e83-49af-97e0-66648d020ccb",
            "affa7db3-34db-4f19-aca3-afae012f47b4",
            "c0570ecd-b0f1-4cdf-b71a-a558cdef866d",
            "032f782b-2b99-4da4-8fcd-8dae8a207d7d"
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(10,15,12,13,8,14),
        'name': 'Seraphine "Whisper" Vaelith',
        'age': 29,
        'gender': 'Female',
        'alignment': 'True Neutral',
        'background': """Seraphine was raised in the shadows of a noble house—not as a daughter, but as an unknown secret. The illegitimate child of a noble lord and a tavern singer, she was hidden away to avoid scandal. When she was old enough to realise the truth, she fled the estate and disappeared into the city's underworld. There, she honed her skills as a thief and spy, adopting the alias "Whisper." She now sells secrets to the highest bidder, but deep down, she still longs for a life of true belonging.""",
        'traits': [
            'Never speaks louder than a whisper, hence her name',
            'Can move completely silently, even in full armour',
            'Always flicks a dagger between her fingers when thinking'
        ],
        'ideals': [
            'The truth is a weapon more powerful than any blade',
            'Loyalties shift like the wind, but gold never betrays'
        ],
        'bonds': [
            'Carries a locket with a portrait of her mother, the only person she ever trusted',
            'Keeps a ledger of noble scandals, using them for leverage'
        ],
        'flaws': [
            'Struggles to trust even those who mean well',
            'Holds grudges for years',
            'Prone to vanity, using disguises and illusions to appear more noble'
        ],
        'height': '5\'6"',
        'build': 'Slender and agile',
        'skin_tone': 'Olive',
        'hair_color': 'Midnight black',
        'hair_style': 'Elegant but practical, often braided at the back',
        'hair_length': 'Medium',
        'hair_type': 'Straight',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Pale violet',
        'eye_shape': 'Almond',
        'distinguishing_features': 'A small tattoo of a crescent moon just behind her ear',
        'clothing_style': 'Dark leather armour tailored for stealth',
        'clothing_colors': 'Black and deep crimson',
        'clothing_accessories': 'A set of silver lockpicks hidden in her boots',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943925/duunimauvlfozj0v8sb3.png"
        'image': "duunimauvlfozj0v8sb3"
    },
    {
        'race': race_ids['Elf'],
        'character_class': class_ids['Cleric'],
        'character_class_skill_choices': [
            "5fec3a3b-806d-47c5-9101-2fb77832ec18",
            "a9ed3d93-d90a-4cbe-946c-eba444b1c8c4",
        ],
        'character_class_cantrip_choices': [
            "a9db1992-544e-4fe9-8306-704bf0bea062", 
            "27a4aef8-024e-496d-bc0b-17cd6aeee017", 
            "0f136266-9ead-405c-8730-0c0f42b74dc9"
        ],
        'character_class_spell_choices': [
            "ad6c7f3a-6770-497d-91bd-ae164f7cca4b", 
            "02164a46-bc18-4dde-99e9-cfd4d4ca44ac", 
            "eedc57b0-5c91-4254-a8d2-d93cb54b2ad8",
        ],
        'ability_points': format_ability_points(8,13,12,14,15,10),
        'name': 'Eldrin "Stormcaller" Faeloris',
        'age': 275,
        'gender': 'Male',
        'alignment': 'Lawful Good',
        'background': """Eldrin was born beneath a sky of rolling thunder, an omen among his people. Devoted to the god of storms from a young age, he became a wandering cleric, bringing justice to the lawless and guiding lost souls toward redemption. He travels the land wielding the power of the storm itself, both as a healer and a warrior. Though serene on the surface, his fury is as relentless as the storm when facing those who harm the innocent.""",
        'traits': [
            'Speaks in measured, poetic phrases',
            'Prefers to stand in the rain whenever possible',
            'Has an intense, piercing gaze that makes others uneasy'
        ],
        'ideals': [
            'The storm does not rage without purpose—nor do I',
            'Justice must be swift, like lightning in the night'
        ],
        'bonds': [
            'His enchanted warhammer, said to be blessed by his deity',
            'A leather-bound tome containing records of his past battles'
        ],
        'flaws': [
            'Struggles with patience, believing in swift action over deliberation',
            'Views the world in black and white, making compromise difficult',
            'Can be harsh in his judgments, even to friends'
        ],
        'height': '6\'2"',
        'build': 'Tall and imposing',
        'skin_tone': 'Pale with faint blue veins visible beneath',
        'hair_color': 'Silver-white',
        'hair_style': 'Flowing and windblown',
        'hair_length': 'Long',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Bright storm-grey',
        'eye_shape': 'Hooded',
        'distinguishing_features': ' Lightning-shaped scars on his forearms from channeling divine energy',
        'clothing_style': 'Flowing robes with silver embroidery, layered over chainmail',
        'clothing_colors': 'Sky blue and silver',
        'clothing_accessories': 'A cloak that crackles faintly with static when touched',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943916/cxtrb1qgclrswikrjn2b.png"
        'image': "cxtrb1qgclrswikrjn2b"
    },
    {
        'race': race_ids['Dwarf'],
        'character_class': class_ids['Barbarian'],
        'character_class_skill_choices': [
            "f0282ac7-16a8-42c4-a50f-4336db5c0162",
            "57b45a74-aacb-4ea7-9d5d-8219b8f15851",
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(15,14,13,10,12,8),
        'name': ' Borik "The Ember" Ironvein',
        'age': 98,
        'gender': 'Male',
        'alignment': 'Chaotic Neutral',
        'background': """Borik was once a proud warrior of his mountain clan, but everything changed when his homeland was razed in an orcish invasion. Now, he fights not for honour, not for duty, but for sheer survival. The fire of vengeance burns within him, and though his rage fuels his strength, it also consumes him. He wanders from battlefield to battlefield, seeking foes worthy of his wrath, all while haunted by the ghosts of his fallen kin.""",
        'traits': [
            'When angered, his voice booms like a war drum',
            'Always sharpening his weapons, even when unnecessary',
            'Has a deep, unsettling laugh that emerges in combat'
        ],
        'ideals': [
            'Glory is won with blood and steel',
            'If I cannot avenge my people, I will make the world fear my name'
        ],
        'bonds': [
            'Keeps a piece of charred stone from his destroyed homeland',
            'Swore an oath to a dying friend that he would never fall without a fight'
        ],
        'flaws': [
            'Prone to reckless violence, sometimes striking before thinking',
            'Drinks heavily to drown out his sorrow',
            'Hates being underground, despite being a dwarf, as it reminds him of his ruined home'
        ],
        'height': '4\'9"',
        'build': 'Muscular and burly',
        'skin_tone': 'Deep bronze',
        'hair_color': 'Fiery red',
        'hair_style': 'Thick and unkempt',
        'hair_length': 'Medium',
        'hair_type': 'Coily',
        'facial_hair_style': 'Full Beard',
        'facial_hair_length': 'Long',
        'eye_color': 'Golden brown',
        'eye_shape': 'Round',
        'distinguishing_features': 'A jagged burn scar running down his left arm',
        'clothing_style': 'Patchwork leather and fur armour, taken from fallen enemies',
        'clothing_colors': 'Charcoal black and deep crimson',
        'clothing_accessories': 'A heavy iron ring that once belonged to his chieftain',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943919/zdkizpln5opxxxikhrhe.png"
        'image': "zdkizpln5opxxxikhrhe"
    },
    {
        'race': race_ids['Elf'],
        'character_class': class_ids['Bard'],
        'character_class_skill_choices': [
            "d8eb6094-2655-4fdd-bfb4-ed01163c4cf5",
            "f0e83eb0-d3a7-40ee-b1a5-ea146b4dd094",
            "571128ca-be8c-41ac-a90a-41b55c90746f",
        ],
        'character_class_cantrip_choices': [
            "87b8c250-f2cc-4920-9b43-0046a8b34e55",
            "9432fedb-4c67-4b63-8778-ef9c985d0729"
        ],
        'character_class_spell_choices': [
            "52b6c000-7810-4857-988b-81db81185ede", 
            "07e69325-723f-45e1-a632-8a747d835728",
            "ae73cd41-1223-4930-afa4-fbe32556281c",
            "144f983f-0681-4953-b75d-705046f0dcd4",
        ],
        'ability_points': format_ability_points(8,14,12,10,13,15),
        'name': 'Thalia Moonbrook',
        'age': 187,
        'gender': 'Female',
        'alignment': 'Chaotic Good',
        'background': """Thalia grew up in the treetop city of Eldenwood, where she was trained as a historian and keeper of lore. However, she found books and scrolls dull—she wanted to live the stories, not just record them. She left her home behind to travel the world, performing for nobles and commoners alike. With her silver tongue and quick wit, she has talked herself out of execution, into royal feasts, and even past the gates of the Feywild. She carries the songs of old and the whispers of the present, spinning them into magic.""",
        'traits': [
            'Speaks in flowery, poetic phrases, even in casual conversation',
            'Has a song for every situation—whether people want to hear it or not',
            "Cannot resist a good story, whether it's true or false"
        ],
        'ideals': [
            'Life is a song, and I will make mine unforgettable',
            'The greatest truth often lies in the most beautiful lie'
        ],
        'bonds': [
            'A silver flute, gifted by a mysterious fey lord',
            'A book of unfinished songs, some of which seem to write themselves'
        ],
        'flaws': [
            'Struggles to take things seriously, even in dire situations',
            'Holds grudges against critics of her music',
            'Prone to embellishing the truth, even when unnecessary'
        ],
        'height': '5\'7"',
        'build': 'Slim and graceful',
        'skin_tone': 'Pale with a faint golden shimmer',
        'hair_color': 'Platinum blonde',
        'hair_style': 'Gently braided with loose strands framing her face',
        'hair_length': 'Long',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Sky blue',
        'eye_shape': 'Almond',
        'distinguishing_features': 'A series of intricate tattoos resembling sheet music along her arms',
        'clothing_style': 'Flowing, embroidered tunic with elaborate patterns',
        'clothing_colors': 'Deep purple and gold',
        'clothing_accessories': 'A collection of rings, each taken from a different admirer',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943904/ifbvqmphgpejdmxthlal.png"
        'image': "ifbvqmphgpejdmxthlal"
    },
    {
        'race': race_ids['Elf'],
        'character_class': class_ids['Fighter'],
        'character_class_skill_choices': [
            "5fec3a3b-806d-47c5-9101-2fb77832ec18",
            "57b45a74-aacb-4ea7-9d5d-8219b8f15851",
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(15,14,13,10,12,8),
        'name': 'Kaelen Dawnstrider',
        'age': 210,
        'gender': 'Male',
        'alignment': 'Lawful Neutral',
        'background': """Kaelen was raised among the elite warriors of an ancient elven kingdom, trained in the art of war since childhood. He served as a royal bodyguard, sworn to protect his liege with unwavering discipline. But when his kingdom fell to betrayal, Kaelen was forced into exile, now wandering the lands as a mercenary. Honour-bound yet burdened by failure, he seeks to redeem himself by finding a new cause worthy of his blade.""",
        'traits': [
            'Always keeps his weapons in pristine condition',
            'Never breaks a promise once given',
            'Rarely smiles, his expression a constant mask of discipline'
        ],
        'ideals': [
            'A warrior is defined by his discipline, not his strength',
            'Honour above all else'
        ],
        'bonds': [
            'The crest of his fallen kingdom, sewn into his cloak',
            'His longsword, an heirloom passed through generations'
        ],
        'flaws': [
            'Struggles with adapting to less rigid lifestyles',
            'Refuses to forgive those who betray their oaths',
            'Holds himself to impossible standards, never feeling worthy'
        ],
        'height': '6\'1"',
        'build': 'Lean and toned',
        'skin_tone': 'Fair with a faint golden hue',
        'hair_color': 'Platinum blonde',
        'hair_style': 'Tied back into a low warrior’s tail',
        'hair_length': 'Long',
        'hair_type': 'Straight',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Ice blue',
        'eye_shape': 'Almond',
        'distinguishing_features': 'A thin, ceremonial scar running diagonally across his left cheek',
        'clothing_style': 'Ornate but practical elven armour',
        'clothing_colors': 'Silver and dark blue',
        'clothing_accessories': 'A flowing, tattered cloak from his homeland',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943731/vgrxa6sbkpmbqmz7wbus.png"
        'image': "vgrxa6sbkpmbqmz7wbus"
    },
    {
        'race': race_ids['Halfling'],
        'character_class': class_ids['Bard'],
        'character_class_skill_choices': [
            "f0282ac7-16a8-42c4-a50f-4336db5c0162",
            "26cd5299-99a3-42ad-bf86-73c453104a08",
            "c0570ecd-b0f1-4cdf-b71a-a558cdef866d",
        ],
        'character_class_cantrip_choices': [
            "66e4a647-cf9f-442a-9c31-db2ae0483cc4", 
            "53fc449d-2488-418e-b2c9-6dd3162f333f",
        ],
        'character_class_spell_choices': [
            "52b6c000-7810-4857-988b-81db81185ede", 
            "07e69325-723f-45e1-a632-8a747d835728",
            "fb37362f-1985-474e-a399-7401b80ab5d7", 
            "8aa90fa7-7039-4e96-adbf-27fde78da110",
        ],
        'ability_points': format_ability_points(8,14,12,10,13,15),
        'name': 'Liliana "Lily" Fairbrook',
        'age': 24,
        'gender': 'Female',
        'alignment': 'Chaotic Good',
        'background': """Born in a quiet halfling village, Lily always had a restless spirit. Rather than settling into a simple life, she took to the road with her lute and a head full of stories. She has performed in grand castles and seedy taverns alike, charming nobles and outlaws in equal measure. But beneath her cheerful exterior, Lily is a keen observer of the world’s injustices, using her music to inspire rebellion and stir the hearts of the downtrodden.""",
        'traits': [
            'Sings or hums when nervous',
            'Can talk her way out of almost any situation',
            'Loves collecting trinkets from different places she visits'
        ],
        'ideals': [
            'A good story can change the world',
            'Freedom is the sweetest melody'
        ],
        'bonds': [
            'Keeps a tiny silver flute that belonged to her mother',
            'A diary filled with songs, stories, and sketches of her travels'
        ],
        'flaws': [
            'Often bites off more than she can chew, getting in over her head',
            'Struggles to take serious matters seriously',
            'Can be too trusting, believing most people have good hearts'
        ],
        'height': '3\'1"',
        'build': 'Small and sprightly',
        'skin_tone': 'Warm peach',
        'hair_color': 'Chestnut brown',
        'hair_style': 'Soft curls bouncing freely',
        'hair_length': 'Medium',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Hazel',
        'eye_shape': 'Round',
        'distinguishing_features': 'Dimples when she smiles, which is often',
        'clothing_style': 'Colourful, flamboyant travel attire with flowing scarves',
        'clothing_colors': 'Deep purple, gold, and emerald green',
        'clothing_accessories': 'A lute slung across her back, adorned with ribbons',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943722/vkyjh4bzvnxxsba9wnqm.png"
        'image': "vkyjh4bzvnxxsba9wnqm"
    },
    {
        'race': race_ids['Dwarf'],
        'character_class': class_ids['Cleric'],
        'character_class_skill_choices': [
            "d8eb6094-2655-4fdd-bfb4-ed01163c4cf5",
            "540937ab-6c67-4c5f-9102-c8b180729a8e"
        ],
        'character_class_cantrip_choices': [
            "a36bffb7-2ee4-4721-990a-66403a35dcec",
            "87b8c250-f2cc-4920-9b43-0046a8b34e55",
            "a9db1992-544e-4fe9-8306-704bf0bea062"
        ],
        'character_class_spell_choices': [
            "02164a46-bc18-4dde-99e9-cfd4d4ca44ac",
            "07e69325-723f-45e1-a632-8a747d835728",
            "e5c90b9e-9590-4050-9dc7-40f14e2c6ae1"
        ],
        'ability_points': format_ability_points(12,8,14,10,15,13),
        'name': 'Dain "Ironfist" Stoneheart',
        'age': 135,
        'gender': 'Male',
        'alignment': 'Lawful Good',
        'background': """Dain was once a warrior, but after surviving a brutal battle that wiped out his battalion, he found faith in the gods of light and healing. Swearing off reckless violence, he took up the mantle of a cleric, dedicating his life to protecting the weak and mending the wounded. Though peace is his path, he will not hesitate to raise his hammer against darkness when necessary.""",
        'traits': [
            'Prays under his breath before every battle',
            'Has a hearty laugh that echoes through halls',
            'Always insists on a proper feast after a victory'
        ],
        'ideals': [
            'A shield is stronger than a sword',
            'Strength is nothing without compassion'
        ],
        'bonds': [
            'Wears an iron amulet inscribed with the names of fallen comrades',
            'His warhammer, reforged from the shattered remains of his first weapon'
        ],
        'flaws': [
            'Struggles with guilt over his past as a warrior',
            'Can be overprotective of his allies',
            'Holds deep grudges against those who break their oaths'
        ],
        'height': '4\'10"',
        'build': 'Broad and powerful',
        'skin_tone': 'Ruddy, weathered from years of travel',
        'hair_color': 'Dark auburn',
        'hair_style': 'Thick and braided',
        'hair_length': 'Medium',
        'hair_type': 'Coily',
        'facial_hair_style': 'Full Beard',
        'facial_hair_length': 'Long',
        'eye_color': 'Dark brown',
        'eye_shape': 'Hooded',
        'distinguishing_features': 'A burn scar on his left forearm from an old forge accident',
        'clothing_style': 'Sturdy, well-worn priestly robes over chainmail',
        'clothing_colors': 'Deep gold and slate grey',
        'clothing_accessories': 'A thick leather belt with pouches filled with holy relics',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943724/creexshw6p9y21wunt0l.png"
        'image': "creexshw6p9y21wunt0l"
    },
    {
        'race': race_ids['Tiefling'],
        'character_class': class_ids['Wizard'],
        'character_class_skill_choices': [
            "a9ed3d93-d90a-4cbe-946c-eba444b1c8c4",
            "540937ab-6c67-4c5f-9102-c8b180729a8e"
        ],
        'character_class_cantrip_choices': [
            "800ee7cd-fd9e-4145-b01f-d51577e26e02",
            "8a2a3ffd-c383-460a-8db7-ea0abe72c419",
            "66e4a647-cf9f-442a-9c31-db2ae0483cc4",
        ],
        'character_class_spell_choices': [
            "015f97f3-e899-4272-a25f-998eb7a865fb",
            "a5e9330a-f9d0-4a3c-9ace-a6c7a080be42",
            "52c3c347-34c7-4b2d-95be-b6fa9f4f940b",
            "7dab1502-53f2-4020-9a31-cb83d36582cd",
            "ae73cd41-1223-4930-afa4-fbe32556281c",
            "02504055-b348-42af-aa50-757ccb4200da",
        ],
        'ability_points': format_ability_points(8,14,12,15,13,10),
        'name': 'Varian "Ashborn" Draeven',
        'age': 32,
        'gender': 'Male',
        'alignment': 'Neutral Evil',
        'background': """Varian was born under an ill-starred comet, his arrival marked by an inferno that consumed his family home. Raised in an arcane academy, he excelled in the study of fire magic but was cast out after an experiment went too far, reducing a library to cinders. Since then, he has wandered in search of forbidden knowledge, seeking power beyond mortal comprehension. He believes that destruction is merely a path to rebirth and will not hesitate to burn away the old to create something new.""",
        'traits': [
            'Speaks with a slow, deliberate cadence, as if weighing every word',
            'Flames flicker unnaturally in his presence, responding to his emotions',
            'Always smells faintly of smoke'
        ],
        'ideals': [
            'Knowledge is power, and power must be taken',
            'The old world must be reduced to ashes so a new one may rise'
        ],
        'bonds': [
            'Carries a charred tome, the last relic of his arcane studies',
            'His staff, carved from obsidian and warm to the touch'
        ],
        'flaws': [
            'Views people as pawns, useful only if they further his goals',
            'Struggles with controlling his own destructive impulses',
            'Deeply paranoid, always expecting betrayal'
        ],
        'height': '5\'11"',
        'build': 'Lean but wiry',
        'skin_tone': 'Dusky red',
        'hair_color': 'Black with streaks of ember-orange',
        'hair_style': 'Slicked back, slightly wild at the ends',
        'hair_length': 'Short',
        'hair_type': 'Wavy',
        'facial_hair_style': 'Goatee',
        'facial_hair_length': 'Short',
        'eye_color': 'Molten gold',
        'eye_shape': 'Upturned',
        'distinguishing_features': 'Two curved, obsidian-black horns and a faintly glowing rune branded onto his forearm',
        'clothing_style': 'Elegant but slightly singed robes, trimmed with golden embroidery',
        'clothing_colors': 'Black and deep crimson',
        'clothing_accessories': 'A silver ring that grows hot when near magical energy',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943706/hklrzryrt0f2azklyzxm.png"
        'image': "hklrzryrt0f2azklyzxm"
    },
    {
        'race': race_ids['Human'],
        'character_class': class_ids['Cleric'],
        'character_class_skill_choices': [
            "a9ed3d93-d90a-4cbe-946c-eba444b1c8c4",
            "540937ab-6c67-4c5f-9102-c8b180729a8e"
        ],
        'character_class_cantrip_choices': [
            "1954b842-4004-4aa7-84bd-e8eb30fe1744",
            "87b8c250-f2cc-4920-9b43-0046a8b34e55",
            "0f136266-9ead-405c-8730-0c0f42b74dc9"
        ],
        'character_class_spell_choices': [
            "eedc57b0-5c91-4254-a8d2-d93cb54b2ad8",
            "e5c90b9e-9590-4050-9dc7-40f14e2c6ae1",
            "53541979-b39b-46c7-82f5-125820bab4a4"
        ],
        'ability_points': format_ability_points(10,13,12,14,15,8),
        'name': 'Rosalind "Rose" Thornebrook',
        'age': 37,
        'gender': 'Female',
        'alignment': 'Neutral Good',
        'background': """A noblewoman turned wandering healer, Rosalind abandoned a life of luxury after witnessing the suffering of the common folk. She devoted herself to a goddess of mercy and has since walked from village to village, tending to the sick and the wounded. Though gentle in spirit, she has little patience for the arrogance of the wealthy and corrupt. She carries the weight of her past, knowing she once turned a blind eye to suffering before opening her heart to those in need.""",
        'traits': [
            'Always carries fresh herbs and remedies in her satchel',
            'Speaks softly but commands great authority',
            'Sings old hymns when tending to wounds'
        ],
        'ideals': [
            'No life is worth more or less than another',
            'Healing is not just of the body, but of the soul'
        ],
        'bonds': [
            'Wears a pendant of her former house, now scratched and faded',
            'Keeps a ledger of those she has saved, never forgetting a name'
        ],
        'flaws': [
            'Struggles with guilt over her privileged past',
            'Takes on more burdens than she can bear',
            'Dislikes killing, even when necessary'
        ],
        'height': '5\'7"',
        'build': 'Slender but sturdy',
        'skin_tone': 'Fair with freckles',
        'hair_color': 'Auburn',
        'hair_style': 'Neatly braided crown',
        'hair_length': 'Medium',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Soft green',
        'eye_shape': 'Round',
        'distinguishing_features': 'A faded scar across her palm from an old self-inflicted wound',
        'clothing_style': 'Modest but well-made travelling robes, reinforced with leather patches',
        'clothing_colors': 'White and deep blue',
        'clothing_accessories': 'A wooden prayer bead bracelet, worn smooth from use',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943599/bcbovr2ahz0hezuyt2iz.png"
        'image': "bcbovr2ahz0hezuyt2iz"
    },
    {
        'race': race_ids['Half-Elf'],
        'character_class': class_ids['Bard'],
        'character_class_skill_choices': [
            "032f782b-2b99-4da4-8fcd-8dae8a207d7d",
            "d8eb6094-2655-4fdd-bfb4-ed01163c4cf5",
            "3bbcebbe-8e83-49af-97e0-66648d020ccb",
            "affa7db3-34db-4f19-aca3-afae012f47b4"
        ],
        'character_class_cantrip_choices': [
            "227a3f45-39c1-441e-9185-aca770d55827", 
            "93c2d7d6-6f3b-4d01-a694-f3ebe804fdc7",
        ],
        'character_class_spell_choices': [
            "f3f8ead5-3969-41a6-a863-09f18811dde1", 
            "49868ff5-11a5-4d9f-b70d-adca9fec1f34", 
            "fb37362f-1985-474e-a399-7401b80ab5d7", 
            "8aa90fa7-7039-4e96-adbf-27fde78da110",
        ],
        'ability_points': format_ability_points(10,15,12,13,8,14),
        'name': 'Jarek "The Fox" Lorran',
        'age': 26,
        'gender': 'Male',
        'alignment': 'Chaotic Neutral',
        'background': """Jarek grew up on the streets, surviving by his wits, charm, and a well-timed joke. He made a name for himself as a performer, conman, and occasional spy, slipping in and out of noble courts and bandit dens alike. Always one step ahead of trouble, he treats life as a grand performance, with himself as the star. He may have stolen a few too many secrets, though, and now certain powerful figures would rather see him silenced permanently.""",
        'traits': [
            'Talks fast, always ready with a quip',
            'Has a tendency to flip a coin between his fingers when thinking',
            'Rarely stays in one place for long'
        ],
        'ideals': [
            'Life is a game—play it well',
            'Loyalty is a currency, and I spend mine wisely'
        ],
        'bonds': [
            'His lucky silver coin, which he swears always lands in his favour',
            'A dagger once belonging to a noble who wants him dead'
        ],
        'flaws': [
            'Gambles compulsively, often losing more than he wins',
            "Can't resist a good heist, even when it's unwise",
            'Tends to talk his way into trouble faster than he can escape it'
        ],
        'height': '5\'10"',
        'build': 'Lean and athletic',
        'skin_tone': 'Light tan',
        'hair_color': 'Dark brown',
        'hair_style': 'Messy but stylish, always looking slightly windswept',
        'hair_length': 'Medium',
        'hair_type': 'Straight',
        'facial_hair_style': 'Stubble',
        'facial_hair_length': '',
        'eye_color': 'Amber',
        'eye_shape': 'Hooded',
        'distinguishing_features': 'A faint scar across his left eyebrow, earned in a duel he technically lost',
        'clothing_style': 'A mix of noble and streetwear, tailored but slightly worn',
        'clothing_colors': 'Dark red and charcoal grey',
        'clothing_accessories': 'A small deck of playing cards, each marked for tricks',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943536/n1jhefsiyr3qondtq6xt.png"
        'image': "n1jhefsiyr3qondtq6xt"
    },
    {
        'race': race_ids['Dwarf'],
        'character_class': class_ids['Fighter'],
        'character_class_skill_choices': [
            "fc38c64c-bc06-4fd1-b38e-3912d517635d",
            "46323de2-37a8-4b4e-9b63-63bec924f21c"
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(15,10,14,8,13,12),
        'name': 'Thrain Ironfist',
        'age': 112,
        'gender': 'Male',
        'alignment': 'Lawful Neutral',
        'background': """Born into the Ironfist clan, Thrain was raised among the forges of a mighty dwarven citadel. His father, a legendary smith, wanted him to follow in his footsteps, but Thrain was drawn to battle rather than craftsmanship. Trained by the fortress guard, he excelled in combat, earning a reputation for his endurance and discipline. During a goblin raid, he led a desperate defence, proving his worth as a warrior. However, a betrayal from within the clan left him disillusioned with politics, and he now roams as a mercenary, seeking honour through steel rather than words.""",
        'traits': [
            'Unyielding in battle, refusing to retreat even when wounded',
            'Has a deep respect for craftsmanship, often appraising weapons and armour',
            'Gruff but loyal to those he deems worthy'
        ],
        'ideals': [
            'Honour is earned through combat, not words',
            'Trust is built through action, not lineage'
        ],
        'bonds': [
            'Carries a war axe forged by his father, refusing to wield any other weapon',
            'Seeks to restore his clan’s honour by tracking down the betrayer'
        ],
        'flaws': [
            'Struggles to let go of grudges',
            'Unwilling to accept help, seeing it as a weakness'
        ],
        'height': '4\'8"',
        'build': 'Stocky and broad-shouldered',
        'skin_tone': 'Deep tan',
        'hair_color': 'Dark brown',
        'hair_style': 'Thick, swept back',
        'hair_length': 'Long',
        'hair_type': 'Wavy',
        'facial_hair_style': 'Full Beard',
        'facial_hair_length': 'Long',
        'eye_color': 'Blue',
        'eye_shape': 'Hooded',
        'distinguishing_features': 'A deep scar over his left eyebrow',
        'clothing_style': 'Heavy, well-maintained armour with a red cloak',
        'clothing_colors': 'Iron-grey with red accents',
        'clothing_accessories': 'A thick leather belt with dwarven runes engraved on the buckle',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943479/wjnqqjkq50iousxmou0f.png"
        'image': "wjnqqjkq50iousxmou0f"
    },
    {
        'race': race_ids['Elf'],
        'character_class': class_ids['Wizard'],
        'character_class_skill_choices': [
            "5fec3a3b-806d-47c5-9101-2fb77832ec18",
            "f0e83eb0-d3a7-40ee-b1a5-ea146b4dd094",
        ],
        'character_class_cantrip_choices': [
            "981bba4e-734c-49fb-8570-0e2c092d8f58",
            "66e4a647-cf9f-442a-9c31-db2ae0483cc4",
            "b692b950-1530-4112-81a3-710f723d9612",
        ],
        'character_class_spell_choices': [
            "ba948243-4881-44de-ad9a-e0f55044159f", 
            "e5c90b9e-9590-4050-9dc7-40f14e2c6ae1", 
            "f3f8ead5-3969-41a6-a863-09f18811dde1",
            "34096cb5-f267-4ccf-8356-7ee396eb2fec", 
            "8d25c369-8660-47ba-a67d-c54a1e56ff2f", 
            "7dab1502-53f2-4020-9a31-cb83d36582cd",
        ],
        'ability_points': format_ability_points(8,13,12,15,14,10),
        'name': 'Sylwen Faelivrin',
        'age': 243,
        'gender': 'Female',
        'alignment': 'Neutral Good',
        'background': """Born under the moonlit boughs of an ancient elven city, Sylwen was always more curious than her peers. She sought knowledge in every shadowed ruin and forgotten tome, eventually joining the Arcane Circle. Her obsession with lost magic led her to a hidden vault containing an ancient grimoire—one that whispered secrets she was not meant to hear. Expelled from the Circle for her reckless pursuit, she now wanders the land, trying to atone for her arrogance by using her knowledge for good while resisting the temptation of the forbidden spells she has uncovered.""",
        'traits': [
            'Soft-spoken but incredibly perceptive',
            'Has an encyclopaedic knowledge of history and arcane lore',
            'Enjoys solving puzzles and riddles'
        ],
        'ideals': [
            'Knowledge should be shared, not hoarded',
            'Magic is a tool, not a crutch'
        ],
        'bonds': [
            'eeks to redeem herself in the eyes of her former mentor',
            'Protects the ancient grimoire, fearing what could happen if it falls into the wrong hands'
        ],
        'flaws': [
            'Prone to overthinking, sometimes freezing in critical moments',
            'Can come across as condescending without meaning to'
        ],
        'height': '5\'9"',
        'build': 'Slim and graceful',
        'skin_tone': 'Pale ivory',
        'hair_color': 'Silver blonde',
        'hair_style': 'Braided into an intricate updo',
        'hair_length': 'Long',
        'hair_type': 'Straight',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Emerald green',
        'eye_shape': 'Almond',
        'distinguishing_features': 'Arcane runes faintly glow along her forearms when she casts spells',
        'clothing_style': 'Flowing robes embroidered with silver filigree',
        'clothing_colors': 'Deep blue with silver accents',
        'clothing_accessories': 'A moonstone pendant that pulses with arcane energy',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943398/sc0vla9zhjx8s1evnxcc.png"
        'image': "sc0vla9zhjx8s1evnxcc"
    },
    {
        'race': race_ids['Human'],
        'character_class': class_ids['Rogue'],
        'character_class_skill_choices': [
            "5fec3a3b-806d-47c5-9101-2fb77832ec18",
            "57b45a74-aacb-4ea7-9d5d-8219b8f15851",
            "fc38c64c-bc06-4fd1-b38e-3912d517635d",
            "c0570ecd-b0f1-4cdf-b71a-a558cdef866d",
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(10,15,14,13,8,12),
        'name': 'Roderic "Rook" Fairweather',
        'age': 29,
        'gender': 'Male',
        'alignment': 'Chaotic Neutral',
        'background': """Rook grew up in the slums of a bustling city, where survival meant being faster, smarter, and more ruthless than the rest. An orphan turned pickpocket, he was eventually taken in by the notorious Nightshade Guild, mastering the art of deception and burglary. His luck changed when he unknowingly stole from a noble with connections to powerful mages. Now marked as a wanted man, Rook is constantly on the move, balancing his wit and charm to stay one step ahead while still indulging in the thrill of the heist.""",
        'traits': [
            'Quick-witted with a sharp tongue',
            'A natural gambler, always testing his luck',
            'Moves like a shadow, rarely seen unless he wants to be'
        ],
        'ideals': [
            'Freedom is the only thing worth fighting for',
            'If you’re good at something, never do it for free'
        ],
        'bonds': [
            'Holds onto a lucky silver coin, a gift from the only person who ever cared for him',
            'Seeks revenge against the noble who ruined his life'
        ],
        'flaws': [
            'Overconfident, often biting off more than he can chew',
            'Struggles with trust, assuming betrayal is inevitable'
        ],
        'height': '5\'11"',
        'build': 'Lean and athletic',
        'skin_tone': 'Light olive',
        'hair_color': 'Dark brown',
        'hair_style': 'Messy, slightly tousled',
        'hair_length': 'Medium',
        'hair_type': 'Wavy',
        'facial_hair_style': 'Stubble',
        'facial_hair_length': '',
        'eye_color': 'Hazel',
        'eye_shape': 'Round',
        'distinguishing_features': 'A thin scar running from his jawline to his collarbone',
        'clothing_style': 'Dark, well-fitted leather with hidden pockets',
        'clothing_colors': 'Black and charcoal grey',
        'clothing_accessories': 'A set of lockpicks hidden in his belt buckle',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943343/foxjah2hyyqc8zbjzflx.png"
        'image': "foxjah2hyyqc8zbjzflx"
    },
    {
        'race': race_ids['Tiefling'],
        'character_class': class_ids['Bard'],
        'character_class_skill_choices': [
            "3bbcebbe-8e83-49af-97e0-66648d020ccb",
            "c0570ecd-b0f1-4cdf-b71a-a558cdef866d",
            "f0e83eb0-d3a7-40ee-b1a5-ea146b4dd094",
        ],
        'character_class_cantrip_choices': [
            "66e4a647-cf9f-442a-9c31-db2ae0483cc4", 
            "53fc449d-2488-418e-b2c9-6dd3162f333f",
        ],
        'character_class_spell_choices': [
            "ad6c7f3a-6770-497d-91bd-ae164f7cca4b",
            "e5c90b9e-9590-4050-9dc7-40f14e2c6ae1",
            "fb37362f-1985-474e-a399-7401b80ab5d7",
            "ae73cd41-1223-4930-afa4-fbe32556281c"
        ],
        'ability_points': format_ability_points(10,14,12,8,13,15),
        'name': 'Seraphine Duskrend',
        'age': 26,
        'gender': 'Female',
        'alignment': 'Chaotic Good',
        'background': """Born under a bad omen in a superstitious village, Seraphine was cast out as a child due to her infernal heritage. She survived on the kindness of travelling performers, who took her in and taught her music, storytelling, and the art of persuasion. Over the years, she honed her craft, using her silver tongue to navigate high society and back-alley dealings alike. Now, she travels the world, singing songs of rebellion and love, exposing corruption where she finds it. She is both adored and feared—her ballads have started revolutions, and those in power whisper her name with dread.""",
        'traits': [
            'Charismatic and theatrical, commanding attention wherever she goes',
            'Has a sharp wit and an even sharper tongue',
            'A hopeless romantic, falling in and out of love wherever she travels'
        ],
        'ideals': [
            'Words can be more powerful than weapons',
            'Every person has a story worth telling'
        ],
        'bonds': [
            'Cherishes a worn lute given to her by the first person who ever showed her kindness',
            'Protects fellow outcasts and misfits, seeing them as her true family'
        ],
        'flaws': [
            'Struggles with commitment, always chasing the next adventure',
            'Prone to making enemies in high places with her provocative songs'
        ],
        'height': '5\'7"',
        'build': 'Slender but toned',
        'skin_tone': 'Deep crimson',
        'hair_color': 'Midnight black',
        'hair_style': 'Wild and windswept',
        'hair_length': 'Long',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Golden amber',
        'eye_shape': 'Upturned',
        'distinguishing_features': 'Small curved horns and a tail that twitches when she lies',
        'clothing_style': 'Flamboyant and stylish, favouring flowing coats and dramatic collars',
        'clothing_colors': 'Deep purples, blacks, and golds',
        'clothing_accessories': 'A silver ring with an unknown sigil, said to grant her luck',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943255/ccvqlw6hntuzhatvsxmx.png"
        'image': "ccvqlw6hntuzhatvsxmx"
    },
    {
        'race': race_ids['Halfling'],
        'character_class': class_ids['Rogue'],
        'character_class_skill_choices': [
            "5fec3a3b-806d-47c5-9101-2fb77832ec18",
            "57b45a74-aacb-4ea7-9d5d-8219b8f15851",
            "f0e83eb0-d3a7-40ee-b1a5-ea146b4dd094",
            "fc38c64c-bc06-4fd1-b38e-3912d517635d",
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(8,15,13,14,10,12),
        'name': 'Brynn Thistledown',
        'age': 24,
        'gender': 'Female',
        'alignment': 'Chaotic Neutral',
        'background': """Brynn grew up in a small halfling village where life was simple and safe—too safe for her liking. Always drawn to excitement, she ran away as a teenager and found herself in a bustling city filled with opportunity and danger. She quickly learned to survive through wit, charm, and quick hands, eventually becoming a skilled thief and con artist. Though she enjoys the thrill of the heist, she follows her own moral code—she never steals from those who can’t afford to lose and occasionally "redistributes" wealth from the corrupt to those in need.""",
        'traits': [
            "Incredibly nimble, slipping through crowds unnoticed",
            "Quick-tongued, always ready with a clever remark or a bold lie",
            "Enjoys pushing her luck, often taking risks just for the thrill"
        ],
        'ideals': [
            "Life is too short to play it safe",
            "The world belongs to those clever enough to take it"
        ],
        'bonds': [
            "Holds onto a tiny wooden charm carved by her younger sister, whom she hopes to reunite with one day",
            "Owes a favour to a dangerous crime lord who once saved her life"
        ],
        'flaws': [
            "Can’t resist a good gamble, even when she knows the odds are against her",
            "Struggles to trust others, assuming everyone has an angle"
        ],
        'height': '3\'2"',
        'build': 'Slim and wiry',
        'skin_tone': 'Fair with a light dusting of freckles',
        'hair_color': 'Auburn',
        'hair_style': 'Messy, often tucked under a hood',
        'hair_length': 'Short',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Bright green',
        'eye_shape': 'Round',
        'distinguishing_features': 'A small scar on her cheek from a botched pickpocket attempt',
        'clothing_style': 'Dark, practical clothing designed for stealth',
        'clothing_colors': 'Black and dark green',
        'clothing_accessories': 'A belt filled with hidden pockets and tiny lockpicks',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943160/ha9qcex8n491olyixp1p.png"
        'image': "ha9qcex8n491olyixp1p"
    },
    {
        'race': race_ids['Dwarf'],
        'character_class': class_ids['Cleric'],
        'character_class_skill_choices': [
            "affa7db3-34db-4f19-aca3-afae012f47b4",
            "540937ab-6c67-4c5f-9102-c8b180729a8e"
        ],
        'character_class_cantrip_choices': [
            "87b8c250-f2cc-4920-9b43-0046a8b34e55", 
            "d535e9f5-9ae8-46d0-8b55-ab85b9689729", 
            "a9db1992-544e-4fe9-8306-704bf0bea062",
        ],
        'character_class_spell_choices': [
            "eedc57b0-5c91-4254-a8d2-d93cb54b2ad8", 
            "07e69325-723f-45e1-a632-8a747d835728", 
            "62634aad-3754-4ea3-be95-2708ebdab3a7",
        ],
        'ability_points': format_ability_points(10,13,14,8,15,12),
        'name': 'Orik Stoneheart',
        'age': 145,
        'gender': 'Male',
        'alignment': 'Lawful Good',
        'background': """Born into a family of devout clerics, Orik always knew he was destined to serve his god. However, unlike his predecessors who remained in grand temples, he felt his duty was to walk among the people, offering aid where needed. After years of service healing the wounded and protecting the innocent, he now roams the land, acting as both a healer and a warrior against darkness. Though he is stubborn and unyielding in his beliefs, he has a deep love for ale, stories, and companionship.""",
        'traits': [
            "Stoic and disciplined, always maintaining his composure",
            "Deeply protective of his allies, treating them like family",
            "Surprisingly humorous when in good company"
        ],
        'ideals': [
            "Strength comes not just from steel, but from faith",
            "The strong should protect the weak, no matter the cost"
        ],
        'bonds': [
            "Swore an oath to defend a sacred relic, which he carries hidden beneath his armour",
            "Seeks to redeem a fallen comrade who turned to darkness"
        ],
        'flaws': [
            "Can be overly rigid, refusing to compromise his beliefs",
            "Has little patience for those who lack discipline"
        ],
        'height': '4\'6"',
        'build': 'Stocky and muscular',
        'skin_tone': 'Ruddy and weathered',
        'hair_color': 'Iron grey',
        'hair_style': 'Thick and swept back',
        'hair_length': 'Long',
        'hair_type': 'Wavy',
        'facial_hair_style': 'Full Beard',
        'facial_hair_length': 'Long',
        'eye_color': 'Dark brown',
        'eye_shape': 'Hooded',
        'distinguishing_features': 'A jagged scar running down his nose',
        'clothing_style': 'Heavy plate armour adorned with religious symbols',
        'clothing_colors': 'Silver and deep blue',
        'clothing_accessories': 'A warhammer engraved with holy runes',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738943078/ltxuvo3xu9rkcqy4pmpc.png"
        'image': "ltxuvo3xu9rkcqy4pmpc"
    },
    {
        'race': race_ids['Human'],
        'character_class': class_ids['Bard'],
        'character_class_skill_choices': [
            "3bbcebbe-8e83-49af-97e0-66648d020ccb",
            "0cf988cb-ed38-40f8-948f-91b679cf502c",
            "5fec3a3b-806d-47c5-9101-2fb77832ec18",
        ],
        'character_class_cantrip_choices': [
            "9432fedb-4c67-4b63-8778-ef9c985d0729",
            "53fc449d-2488-418e-b2c9-6dd3162f333f",
        ],
        'character_class_spell_choices': [
            "07e69325-723f-45e1-a632-8a747d835728", 
            "e5c90b9e-9590-4050-9dc7-40f14e2c6ae1",
            "fb37362f-1985-474e-a399-7401b80ab5d7", 
            "8aa90fa7-7039-4e96-adbf-27fde78da110",
        ],
        'ability_points': format_ability_points(10,13,14,8,12,15),
        'name': 'Lysara Valmont',
        'age': 31,
        'gender': 'Female',
        'alignment': 'Neutral Good',
        'background': """Lysara was raised in a noble household where she was expected to marry well and uphold the family name. Instead, she abandoned her gilded cage and chose a life of adventure, seeking inspiration for her songs in the real world rather than courtly halls. A skilled musician and storyteller, she now travels from city to city, earning coin with her performances and uncovering forgotten legends. She has a particular fondness for exposing corruption and bringing hope to the downtrodden through her tales.""",
        'traits': [
            "Charismatic and effortlessly charming",
            "Has an encyclopaedic knowledge of myths and folklore",
            "Always finds a way to make people laugh, even in dire situations"
        ],
        'ideals': [
            "Stories have the power to change the world",
            "Truth and beauty should never be silenced"
        ],
        'bonds': [
            "Still carries an old locket from her childhood, a reminder of the family she left behind",
            "Seeks to write the greatest epic the world has ever known"
        ],
        'flaws': [
            "Has difficulty staying in one place for too long, always chasing the next story",
            "Often gets herself into trouble by speaking out against the powerful"
        ],
        'height': '5\'6"',
        'build': 'Slender and graceful',
        'skin_tone': 'Warm beige',
        'hair_color': 'Chestnut brown',
        'hair_style': 'Elegantly styled into loose curls',
        'hair_length': 'Long',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Sapphire blue',
        'eye_shape': 'Upturned',
        'distinguishing_features': 'A delicate tattoo of a quill on her wrist',
        'clothing_style': 'Elegant, flowing dresses with intricate embroidery',
        'clothing_colors': 'Deep red and gold',
        'clothing_accessories': 'A silver charm bracelet with tiny musical notes',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738942987/ybaxyp7wn8dgebxpnmn9.png"
        'image': "ybaxyp7wn8dgebxpnmn9"
    },
    {
        'race': race_ids['Elf'],
        'character_class': class_ids['Wizard'],
        'character_class_skill_choices': [
            "5fec3a3b-806d-47c5-9101-2fb77832ec18",
            "f0e83eb0-d3a7-40ee-b1a5-ea146b4dd094",
        ],
        'character_class_cantrip_choices': [
            "53fc449d-2488-418e-b2c9-6dd3162f333f", 
            "6ed84f5f-d26a-426e-a1e3-99ac71dcfb47", 
            "227a3f45-39c1-441e-9185-aca770d55827",
        ],
        'character_class_spell_choices': [
            "ba948243-4881-44de-ad9a-e0f55044159f", 
            "e5c90b9e-9590-4050-9dc7-40f14e2c6ae1", 
            "f3f8ead5-3969-41a6-a863-09f18811dde1", 
            "fb37362f-1985-474e-a399-7401b80ab5d7", 
            "79d4e2a3-96c2-499f-b0dd-154fadb132cf", 
            "02504055-b348-42af-aa50-757ccb4200da",
        ],
        'ability_points': format_ability_points(8,14,12,15,10,13),
        'name': 'Vaelin Duskwhisper',
        'age': 132,
        'gender': 'Male',
        'alignment': 'Neutral Good',
        'background': """Vaelin was raised in an ancient elven enclave, where he studied the arcane arts from a young age. A prodigy among his peers, he excelled in spellcraft but was always more fascinated by lost knowledge than tradition. His pursuit of forgotten magic led him to leave his homeland in search of ancient ruins, forbidden tomes, and the secrets of the cosmos. Now, he travels the world, seeking wisdom and protecting knowledge from those who would misuse it.""",
        'traits': [
            'Highly intelligent and analytical, always thinking several steps ahead.',
            'Soft-spoken but precise in his words, valuing knowledge over conflict.',
            'Has a deep respect for history and forgotten cultures.'
        ],
        'ideals': [
            'Knowledge must be preserved and shared with those who will use it wisely.',
            'True power lies in understanding, not in brute strength.'
        ],
        'bonds': [
            'Carries a small silver pendant given to him by his first mentor, a reminder of his duty to wisdom.',
            'Feels responsible for a former apprentice who turned to dark magic.'
        ],
        'flaws': [
            'Prone to overthinking and sometimes hesitant to act in crucial moments.',
            'Can come across as aloof or dismissive when dealing with those he considers ignorant.'
        ],
        'height': "5'10\"",
        'build': 'Lean and graceful',
        'skin_tone': 'Pale with a faint golden hue',
        'hair_color': 'Silver-white',
        'hair_style': 'Tied back in an intricate braid',
        'hair_length': 'Long',
        'hair_type': 'Straight',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Deep violet',
        'eye_shape': 'Almond',
        'distinguishing_features': 'Delicate arcane runes tattooed along his forearms, glowing faintly when he casts spells.',
        'clothing_style': 'Elegant robes embroidered with celestial patterns',
        'clothing_colors': 'Deep blue and silver',
        'clothing_accessories': 'A leather-bound spellbook chained to his belt, filled with his own arcane discoveries',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738942883/cqry1g8vmctwmetvt5my.png"
        'image': "cqry1g8vmctwmetvt5my"
    },
    {
        'race': race_ids['Dwarf'],
        'character_class': class_ids['Fighter'],
        'character_class_skill_choices': [
            "26cd5299-99a3-42ad-bf86-73c453104a08",
            "0cf988cb-ed38-40f8-948f-91b679cf502c",
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(15,12,14,10,13,8),
        'name': 'Rurik Ironfist',
        'age': 157,
        'gender': 'Male',
        'alignment': 'Lawful Neutral',
        'background': (
            "Born into a proud line of warriors, Rurik was raised with an axe in his hands and duty in his heart. "
            "He served as a soldier in his clan’s army, defending their mountain stronghold from invaders and monstrous threats. "
            "After a disastrous battle where his entire unit was wiped out, Rurik left his homeland to seek redemption, vowing "
            "never to let his comrades fall again. Now, he wanders the land as a mercenary, searching for a cause worthy of his blade."
        ),
        'traits': [
            'Disciplined and methodical, treating combat like an art.',
            'Speaks bluntly, believing honesty is the greatest virtue.',
            'Enjoys a good drink but never allows himself to lose control.'
        ],
        'ideals': [
            'Strength and honour define a warrior’s worth.',
            'Loyalty to one’s comrades is the highest duty.'
        ],
        'bonds': [
            'Wears the broken insignia of his fallen unit as a constant reminder of his oath.',
            'Seeks to reclaim his family’s lost ancestral weapon, stolen during an orc raid.'
        ],
        'flaws': [
            'Struggles to forgive himself for past failures, carrying guilt like a heavy burden.',
            'Slow to trust outsiders, believing actions speak louder than words.'
        ],
        'height': "4'8\"",
        'build': 'Broad and muscular',
        'skin_tone': 'Bronzed from years of exposure to forge and battlefield',
        'hair_color': 'Dark brown with streaks of grey',
        'hair_style': 'Thick and slightly unkempt',
        'hair_length': 'Medium',
        'hair_type': 'Wavy',
        'facial_hair_style': 'Full Beard',
        'facial_hair_length': 'Long',
        'eye_color': 'Dark grey',
        'eye_shape': 'Hooded',
        'distinguishing_features': 'A deep scar running across his left cheek from an old battle wound.',
        'clothing_style': 'Heavy plate armour adorned with clan emblems',
        'clothing_colors': 'Iron grey and crimson',
        'clothing_accessories': 'A thick leather belt with dwarven runes carved into the buckle',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738942777/r73ns7bfp1eigrjxefav.png"
        'image': "r73ns7bfp1eigrjxefav"
    },
    {
        'race': race_ids['Tiefling'],
        'character_class': class_ids['Rogue'],
        'character_class_skill_choices': [
            "78f8567e-8c82-4f41-ae7e-112a299dd0aa",
            "5fec3a3b-806d-47c5-9101-2fb77832ec18",
            "fc38c64c-bc06-4fd1-b38e-3912d517635d",
            "3bbcebbe-8e83-49af-97e0-66648d020ccb"
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(10,15,13,8,12,14),
        'name': 'Zyra Vex',
        'age': 29,
        'gender': 'Female',
        'alignment': 'Chaotic Neutral',
        'background': (
            "Born in the slums and abandoned as a child, Zyra learned early that the world belonged to those willing to take what they needed. "
            "She honed her skills in the shadows, becoming an expert thief and assassin, taking contracts on the wealthy and corrupt. "
            "Despite her sharp tongue and colder demeanour, she has a soft spot for the desperate and downtrodden, often leaving a portion of her earnings "
            "to aid street orphans. Whether she’s robbing nobles or slipping through city guards unnoticed, Zyra lives by one rule: trust no one."
        ),
        'traits': [
            'Cunning and observant, always watching for an advantage.',
            'Prefers action over words, believing hesitation is weakness.',
            'Enjoys the thrill of danger, often taking risks just to feel alive.'
        ],
        'ideals': [
            'Freedom is the only thing worth fighting for.',
            'Survival isn’t about strength—it’s about wit.'
        ],
        'bonds': [
            'Carries a silver coin engraved with a strange symbol, the only clue to her unknown parentage.',
            'Owes a life debt to an old mentor who once saved her from execution.'
        ],
        'flaws': [
            'Struggles to trust others, always expecting betrayal.',
            'Often lets her pride push her into reckless situations.'
        ],
        'height': "5'5\"",
        'build': 'Lithe and athletic',
        'skin_tone': 'Deep purple',
        'hair_color': 'Jet black',
        'hair_style': 'Sleek and straight',
        'hair_length': 'Long',
        'hair_type': 'Straight',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Fiery orange',
        'eye_shape': 'Upturned',
        'distinguishing_features': 'Small, sharp horns curling back over her temples and a forked tail.',
        'clothing_style': 'Dark, fitted leather designed for stealth',
        'clothing_colors': 'Black and deep red',
        'clothing_accessories': 'A set of throwing knives strapped to her thigh',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738942629/ghznf6wqtgkxp8zakzgf.png"
        'image': "ghznf6wqtgkxp8zakzgf"
    },
    {
        'race': race_ids['Half-Elf'],
        'character_class': class_ids['Bard'],
        'character_class_skill_choices': [
            "c0570ecd-b0f1-4cdf-b71a-a558cdef866d",
            "032f782b-2b99-4da4-8fcd-8dae8a207d7d",
            "f0e83eb0-d3a7-40ee-b1a5-ea146b4dd094",
            "3bbcebbe-8e83-49af-97e0-66648d020ccb"
        ],
        'character_class_cantrip_choices': [
            "93c2d7d6-6f3b-4d01-a694-f3ebe804fdc7", 
            "9432fedb-4c67-4b63-8778-ef9c985d0729"
        ],
        'character_class_spell_choices': [
            "e5c90b9e-9590-4050-9dc7-40f14e2c6ae1", 
            "f3f8ead5-3969-41a6-a863-09f18811dde1",
            "c3ed0baf-992e-40af-a969-071e8e641da7", 
            "ae73cd41-1223-4930-afa4-fbe32556281c"
        ],
        'ability_points': format_ability_points(8,13,14,12,10,15),
        'name': 'Elias Thornbrook',
        'age': 37,
        'gender': 'Male',
        'alignment': 'Neutral Good',
        'background': (
            "Elias was born to an elven diplomat and a human bard, growing up in the midst of courtly intrigue and artistic expression. "
            "From a young age, he was drawn to music, using his natural charm to navigate both noble courts and shady taverns. "
            "Over time, he became a travelling minstrel, collecting stories and uncovering long-forgotten tales. "
            "Though he enjoys the pleasures of life, his true passion lies in using his music to inspire hope and rebellion."
        ),
        'traits': [
            'Charming and effortlessly persuasive, able to talk his way out of most situations.',
            'Lover of stories, always eager to hear or tell a good tale.',
            'Has a mischievous streak, enjoying harmless pranks and jokes.'
        ],
        'ideals': [
            'Music and art can change the world.',
            'The pen is mightier than the sword, but both have their uses.'
        ],
        'bonds': [
            'Cherishes an old, weathered lute passed down from his father.',
            'Seeks to reunite with a lost love, leaving secret messages in his songs in hopes they will hear.'
        ],
        'flaws': [
            'A hopeless romantic, often falling for people who are bad for him.',
            'Has trouble committing to a cause, always chasing the next great story.'
        ],
        'height': "5'11\"",
        'build': 'Lean and toned',
        'skin_tone': 'Fair with a slight olive undertone',
        'hair_color': 'Golden blonde',
        'hair_style': 'Loose waves that frame his face',
        'hair_length': 'Medium',
        'hair_type': 'Wavy',
        'facial_hair_style': 'Stubble',
        'facial_hair_length': '',
        'eye_color': 'Emerald green',
        'eye_shape': 'Almond',
        'distinguishing_features': 'A faint scar along his jawline from a duel gone wrong.',
        'clothing_style': 'Stylish but practical, favouring embroidered tunics and high boots',
        'clothing_colors': 'Royal blue and silver',
        'clothing_accessories': 'A silver ring set with a sapphire, said to bring luck to performers',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738942533/swssu7ap5d4vgukdsppr.png"
        'image': "swssu7ap5d4vgukdsppr"
    },
    {
        'race': race_ids['Human'],
        'character_class': class_ids['Cleric'],
        'character_class_skill_choices': [
            "d8eb6094-2655-4fdd-bfb4-ed01163c4cf5",
            "affa7db3-34db-4f19-aca3-afae012f47b4"
        ],
        'character_class_cantrip_choices': [
            "1954b842-4004-4aa7-84bd-e8eb30fe1744", 
            "87b8c250-f2cc-4920-9b43-0046a8b34e55", 
            "d535e9f5-9ae8-46d0-8b55-ab85b9689729",
        ],
        'character_class_spell_choices': [
            "8aa90fa7-7039-4e96-adbf-27fde78da110", 
            "53541979-b39b-46c7-82f5-125820bab4a4", 
            "52c3c347-34c7-4b2d-95be-b6fa9f4f940b",
        ],
        'ability_points': format_ability_points(14,12,13,10,15,8),
        'name': 'Seraphine Valmont',
        'age': 42,
        'gender': 'Female',
        'alignment': 'Lawful Good',
        'background': (
            "Raised in a remote monastery devoted to the goddess of light, Seraphine spent her life tending to the sick and guiding lost souls. "
            "She was once content within the monastery walls, but after witnessing the suffering of the world beyond, she took up her mace and shield "
            "to bring divine justice where it was needed most. Now, she travels from village to village, healing the wounded and smiting the wicked, "
            "a beacon of hope to those in despair."
        ),
        'traits': [
            'Speaks with a calm and reassuring presence, instilling hope in others.',
            'Fiercely protective of the innocent and downtrodden.',
            'Maintains unwavering faith, never doubting her divine purpose.'
        ],
        'ideals': [
            'Compassion and mercy are the greatest strengths one can wield.',
            'Darkness cannot stand where light is brought forth.'
        ],
        'bonds': [
            'Carries a worn holy symbol that once belonged to her mentor.',
            'Swore an oath to never let another innocent fall under her watch.'
        ],
        'flaws': [
            'Struggles with guilt over those she couldn’t save.',
            'Can be overly zealous, sometimes seeing sin where there is none.'
        ],
        'height': "5'7\"",
        'build': 'Strong but graceful',
        'skin_tone': 'Fair with golden undertones',
        'hair_color': 'Auburn',
        'hair_style': 'Swept back into a tight braid',
        'hair_length': 'Long',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Sky blue',
        'eye_shape': 'Almond',
        'distinguishing_features': 'A faint halo-like glow appears around her in moments of deep prayer.',
        'clothing_style': 'Flowing white robes with gold embroidery, layered over chainmail',
        'clothing_colors': 'White and gold',
        'clothing_accessories': 'A silver amulet shaped like a sunburst, signifying her divine patron',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738942312/ey34sghlg6izywhcbyyd.png"
        'image': "ey34sghlg6izywhcbyyd"
    },
    {
        'race': race_ids['Halfling'],
        'character_class': class_ids['Rogue'],
        'character_class_skill_choices': [
            "5fec3a3b-806d-47c5-9101-2fb77832ec18",
            "57b45a74-aacb-4ea7-9d5d-8219b8f15851",
            "f0e83eb0-d3a7-40ee-b1a5-ea146b4dd094",
            "fc38c64c-bc06-4fd1-b38e-3912d517635d",
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(8,15,14,13,12,10),
        'name': 'Milo “Quickfingers” Tealeaf',
        'age': 25,
        'gender': 'Male',
        'alignment': 'Chaotic Good',
        'background': (
            "Born into a family of renowned burglars, Milo was practically raised on the art of thievery. "
            "He never stole out of greed, only from those who hoarded wealth while others suffered. "
            "His carefree attitude and quick wit made him popular among the common folk, though many a noble cursed his name. "
            "Now, he travels from town to town, relieving the rich of their excess gold and slipping a few coins into the pockets of those in need."
        ),
        'traits': [
            'Always has a joke ready, even in the tensest situations.',
            'Loves a good gamble, whether with dice or in life.',
            'Surprisingly kind-hearted despite his criminal tendencies.'
        ],
        'ideals': [
            'The rich have more than they need; it’s only fair to share.',
            'A person’s worth is measured by their deeds, not their birth.'
        ],
        'bonds': [
            'His mother taught him everything he knows about thievery, and he sends her letters detailing his exploits.',
            'Once pulled off a heist with a mysterious masked partner—he still wonders who they were.'
        ],
        'flaws': [
            'Has a hard time resisting a challenge, even when it’s clearly a trap.',
            'Terrible at keeping secrets, especially when drunk.'
        ],
        'height': "3'2\"",
        'build': 'Slim and nimble',
        'skin_tone': 'Warm tan',
        'hair_color': 'Chestnut brown',
        'hair_style': 'Messy and tousled',
        'hair_length': 'Short',
        'hair_type': 'Curly',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Hazel',
        'eye_shape': 'Round',
        'distinguishing_features': 'A small tattoo of a playing card on his wrist, a symbol of his past heists.',
        'clothing_style': 'Dark, close-fitting leathers perfect for sneaking',
        'clothing_colors': 'Black and burgundy',
        'clothing_accessories': 'A lockpicking set hidden in the lining of his vest',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738942154/uomqtlgjqwjb7t5amcly.png"
        'image': "uomqtlgjqwjb7t5amcly"
    },
    {
        'race': race_ids['Elf'],
        'character_class': class_ids['Barbarian'],
        'character_class_skill_choices': [
            "fc38c64c-bc06-4fd1-b38e-3912d517635d",
            "46323de2-37a8-4b4e-9b63-63bec924f21c"
        ],
        'character_class_cantrip_choices': [],
        'character_class_spell_choices': [],
        'ability_points': format_ability_points(15,12,14,8,13,10),
        'name': 'Sylvaris Stormwalker',
        'age': 120,
        'gender': 'Non-binary',
        'alignment': 'Chaotic Neutral',
        'background': (
            "Once a serene forest guardian, Sylvaris was forever changed when their homeland was razed by invaders. "
            "The devastation awakened a primal rage deep within, and they abandoned their old life to embrace the storm within. "
            "Now, they roam the wilds, seeking vengeance for their lost kin and battling those who would exploit nature. "
            "Though rage burns in their heart, echoes of their old self remain, making them a fierce protector of the natural world."
        ),
        'traits': [
            'Has a deep, spiritual connection with nature, often speaking to the wind and trees.',
            'Quick-tempered and fearless, never backing down from a fight.',
            'Despite their fury, shows unexpected gentleness towards animals and children.'
        ],
        'ideals': [
            'The wilds must be protected at all costs.',
            'Strength is not just muscle, but the will to endure.'
        ],
        'bonds': [
            'Wields a massive greataxe crafted from an ancient fallen tree, a relic of their lost home.',
            'Seeks revenge on the warlord who destroyed their homeland.'
        ],
        'flaws': [
            'Finds it difficult to control their rage, sometimes lashing out unpredictably.',
            'Has little patience for civilisation, struggling with laws and rules.'
        ],
        'height': "6'3\"",
        'build': 'Tall and sinewy, with corded muscle',
        'skin_tone': 'Bronzed with deep green tribal tattoos',
        'hair_color': 'Ash blonde',
        'hair_style': 'Worn in intricate braids',
        'hair_length': 'Long',
        'hair_type': 'Wavy',
        'facial_hair_style': 'None',
        'facial_hair_length': '',
        'eye_color': 'Stormy grey',
        'eye_shape': 'Monolid',
        'distinguishing_features': 'A jagged scar running down their left arm, earned in their first great battle.',
        'clothing_style': 'Minimalist, tribal garments made from leather and fur',
        'clothing_colors': 'Earthy browns and deep greens',
        'clothing_accessories': 'A necklace made from the teeth of fallen foes, each one representing a victory',
        #'image_url': "https://res.cloudinary.com/dybgrzu7z/image/upload/v1738942038/imrw0wwm47uvp2ur19ss.png",
        'image': "imrw0wwm47uvp2ur19ss"
    }
]
