def apply(character):
    character.config = {"edition":"5e", "critType":'maxDie'}
    character.name = "Myriil"
    character.baseStats = '8,17,14,10,15,8'
    character.alignment = "Lawful Neutral"
    character.charClass = "Ranger"
    character.level = 4
    character.background = "Spy"
    character.feats = {"Level 4:":"Elven Accuracy", "Gloomstalker Bow":"Sharpshooter"}
    character.race = "Shadar-Kai"
    character.playerName = "Griffin"
    character.armor = {"name" : "Studded Leather", "armorBonus" : 2, "ability":"Dex", "maxAbility": 20, "armorCheck" : 0, "spellFailure" : 0, "modifiers": []}
    character.weapon = [
        {"name" : "Longbow"    , "bonus":0 , "damageDie" : "1d8",  "damageType": "P", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Ammunition","Range(150/600)","Heavy","Two-Handed"] , 'tags':["Ranged"]},
        {"name" : "Shortsword" , "bonus":0 , "damageDie" : "1d6",  "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Finesse","Light"], 'tags':["Melee", "TWF", "Main"]},
        {"name" : "Shortsword" , "bonus":0 , "damageDie" : "1d6",  "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Finesse","Light"], 'tags':["Melee", "TWF", "Off-Hand"]},
    ]

    return character