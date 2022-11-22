id = 2

def apply(character):
    character.id = id
    character.config = {"edition":"5e", "critType":'maxDie',"castingType":"known"}
    character.name = "Myriil Taegen"
    character.baseStats = '8,17,14,10,15,8'
    character.alignment = "Lawful Neutral"
    character.charClass = "Ranger"
    character.level = 4
    character.background = "Spy"
    character.feats = {"Elven Accuracy":"Level 4:", "Sharpshooter":"Gloomstalker Bow"}
    character.race = {"name":"Shadar-Kai", "options":{"primaryAbility":"Dexterity", "secondaryAbility":"Wisdom", "languages":["Elven"]}}
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

    character.flavor = {
        "backstory":"""
            A 527-year-old shadar kai sent by the Raven Queen to stop Strahd and his abominations. When he was sent on this mission he was given a weapon from the Raven Queen
            He knows the true signs of the adventures who will defeat Strahd. He knows they have not come until he meets the current party.
            Before the party came, the townspeople came to him, adamant that they would take on Strahd, they begged Myriil to teach them to fight. He knew they would not defeat him. They were nowhere close to the prophecies he has heard. The townspeople were determined. He trained them as well as he could so they could stand as good of a chance as possible. At least they could have a chance of dying with dignity, with a weapon in their hand, standing their ground.
            The night they planned to execute the Attack on Ravenloft, Myriil left the town, knowing he would not be able to live with the guilt of seeing the aftermath of the attack.
        """,
        "personalityTraits":"""
            Only satisfied with perfection, sometimes even that isnt enough
            Grouchy
        """,
        "ideals":"""
            I will refine my mind and body in pursuit of perfection
        """,
        "flaws":"""
            Grouchy
        """,
        "bonds":"""
            Devoted to his goddess, The Raven Queen
            Will do almost anything to help the party defeat Strahd
        """
    }

    return character