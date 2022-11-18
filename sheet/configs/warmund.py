def apply(character):
    character.config = {"edition":"5e", "critType":'doubleDice',"castingType":"prepared"}
    character.name = "Warmund"
    character.baseStats = '11,16,14,15,12,11'
    character.alignment = "Lawful Neutral"
    character.charClass = "Wizard"
    character.level = 3
    character.background = "Sage"
    character.feats = {}
    character.race = "Harengon"
    character.playerName = "Griffin"
    character.armor = {"name" : "Leather", "armorBonus" : 1, "ability":"Dex", "maxAbility": 20, "armorCheck" : 0, "spellFailure" : 0, "modifiers": []}
    character.weapon = [
        {"name" : "Rapier" , "bonus":0 , "damageDie" : "1d8",  "damageType": "P", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Finesse"], 'tags':["Melee"]},
    ]
    character.equipment = {
        "head"     : {"name":""},
        "headband" : {"name":""},
        "eyes"     : {"name":""},
        "shoulders": {"name":""},
        "neck"     : {"name":""},
        "chest"    : {"name":""},
        "body"     : {"name":""},
        "armor"    : {"name":"Leather", "armorBonus" : 1, "ability":"Dex", "maxAbility": 20, "armorCheck" : 0, "spellFailure" : 0, "modifiers": []},
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
        "flaws":"""
            Grouchy
        """,
        "bonds":"""
            Devoted to his goddess, The Raven Queen
            Will do almost anything to help the party defeat Strahd
        """
    }

    return character