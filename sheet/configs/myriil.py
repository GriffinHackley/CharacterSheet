def apply(character):
    character.config = {"edition":"5e", "critType":'maxDie',"castingType":"prepared"}
    character.name = "Myriil Taegen"
    character.baseStats = '8,17,14,10,15,8'
    character.alignment = "Lawful Neutral"
    character.charClass = "Ranger"
    character.level = 4
    character.background = "Spy"
    character.feats = {"Elven Accuracy":"Level 4:", "Sharpshooter":"Gloomstalker Bow"}
    character.race = "Shadar-Kai"
    character.playerName = "Griffin"
    character.armor = {"name" : "Studded Leather", "armorBonus" : 2, "ability":"Dex", "maxAbility": 20, "armorCheck" : 0, "spellFailure" : 0, "modifiers": []}
    character.weapon = [
        {"name" : "Longbow"    , "bonus":0 , "damageDie" : "1d8",  "damageType": "P", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Ammunition","Range(150/600)","Heavy","Two-Handed"] , 'tags':["Ranged"]},
        {"name" : "Shortsword" , "bonus":0 , "damageDie" : "1d6",  "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Finesse","Light"], 'tags':["Melee", "TWF", "Main"]},
        {"name" : "Shortsword" , "bonus":0 , "damageDie" : "1d6",  "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Finesse","Light"], 'tags':["Melee", "TWF", "Off-Hand"]},
    ]
    character.equipment = {
        "head"     : {"name":""},
        "headband" : {"name":""},
        "eyes"     : {"name":""},
        "shoulders": {"name":""},
        "neck"     : {"name":""},
        "chest"    : {"name":""},
        "body"     : {"name":""},
        "armor"    : {"name":"Studded Leather", "armorBonus" : 2, "ability":"Dex", "maxAbility": 20, "armorCheck" : 0, "spellFailure" : 0, "modifiers": []},
        "belt"     : {"name":""},
        "wrists"   : {"name":""},
        "hands"    : {"name":""},
        "ring1"    : {"name":""},
        "ring2"    : {"name":""},
        "feet"     : {"name":""},
    }

    return character