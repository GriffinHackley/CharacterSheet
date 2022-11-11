def apply(character):
    character.config = {"edition":"Pathfinder", "critType":'doubleAll'}
    character.edition = "Pathfinder"
    character.name = "Nail"
    character.baseStats = '14,16,14,12,16,8'
    character.alignment = "Chaotic Neutral"
    character.charClass = "Warpriest"
    character.level = 4
    character.background = "In Their Footsteps"
    character.feats = {"Level 1:":"Two-Weapon Fighting", "Level 3":"Butterfly Sting", "Warpriest 3":"Combat Reflexes"}
    character.race = "Half-Orc"
    character.playerName = "Griffin"
    character.traits = ["Fate's Favored", "Anatomist"]
    character.armor = {"name" : "Chain Shirt", "armorBonus" : 4, "ability":"Dex", "maxAbility": 4, "armorCheck" : 2, "spellFailure" : 20, "modifiers": []}
    character.weapon = [
        {"name" : "Kukri", "bonus":1, "damageDie" : "1d4", "critRange":"18-20", "critDamage":2, "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Strength' ,'tags':['TWF','Main']},
        {"name" : "Kukri", "bonus":0, "damageDie" : "1d4", "critRange":"18-20", "critDamage":2, "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Strength','tags':['TWF','Off-Hand'] },
        {"name" : "Chakram (30ft.)", "bonus":0, "damageDie" : "1d8", "critRange":"20", "critDamage":2, "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Strength', 'tags':['ranged']},
    ]
    character.equipment = {
        "head"     : "",
        "headband" : "Headband of int",
        "eyes"     : "This is a test",
        "shoulders": "Juggernauts Pauldrons",
        "neck"     : "Amulet of Natural Armor",
        "chest"    : "Something I cant think f",
        "body"     : "This is another test",
        "armor"    : {"name" : "Chain Shirt", "armorBonus" : 4, "ability":"Dex", "maxAbility": 4, "armorCheck" : 2, "spellFailure" : 20, "modifiers": []},
        "belt"     : "Belt of dex",
        "wrists"   : "bracesr of something",
        "hands"    : "handwraps of [unching",
        "ring1"    : "ring of invisilibty",
        "ring2"    : "another ring of invis",
        "feet"     : "boots of speed",
    }
    character.skillRanks = {
        'Heal'         : 1,
        'Handle Animal': 1,
        'Perception'   : 3,
        'Stealth'      : 3,
        'Survival'     : 1,
    }

    return character