id = 3

def apply(character):
    character.id = id
    character.config = {"edition":"5e", "critType":'doubleDice',"castingType":"prepared"}
    character.name = "Warmund"
    character.baseStats = '11,16,14,15,12,11'
    character.alignment = "Lawful Neutral"
    character.charClass = "Wizard"
    character.level = 3
    character.background = "Sage"
    character.feats = {}
    character.race = {"name":"Harengon", "options":{"primaryAbility":"Dexterity", "secondaryAbility":"Intelligence", "languages":["Sylvan"]}}
    character.playerName = "Griffin"
    character.armor = {"name" : "Leather", "armorBonus" : 1, "ability":"Dex", "maxAbility": 20, "armorCheck" : 0, "spellFailure" : 0, "modifiers": []}
    character.weapon = [
        {"name" : "Rapier"       , "bonus":0 , "damageDie" : "1d8",  "damageType": "P"      , "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Finesse"], 'tags':["Melee"]},
        {"name" : "Shadow Blade" , "bonus":0 , "damageDie" : "2d8",  "damageType": "Psychic", "toHitAbility": "Dexterity", "damageAbility": 'Dexterity' ,'properties':["Finesse", "Light", "Thrown (20/60)"], 'tags':["Melee"]},
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
            When Warmund was young, he was bullied for being different. No one in his small town, Yrossa, had ever met a Harengon before. After years of being picked on, he developed a power complex, he wanted power so that no one would ever be able to look down on him again. He began studying magic as a means to obtain more power.
            When Warmund went to the Witchlight Carnival, because of the strange fey magic, his handwriting was stolen by some kind of Shadow Balerina. Whenever he tries to write anything, Warmund can read it just fine. However, anyone else trying to read Warmund's writing will find a jumble of untranslatable symbols.
            He studied diligently and was eventually admitted into the Soltryce Academy where he was permitted to study magic. Trent Ikithon took notice of Warmund because of his peculiar aliment. The symbols that Warmund writes with bear a strange resemblance to the magical encryption on the Tome of Bladesinging. Trent Ikithon recruits Warmund to become a Volstrucker and learn under his tutelage.
            Warmund was sent by Trent Ikithon to the Witchlight Carnival to learn the secrets of the fey magics. As part of this process, Warmund hopes that he will be able to cure himself of his ailment but more importantly decipher the secrets in the Tome of Bladesinging. Warmund has since learned the fundamentals of Bladesinging
        """,
        "personalityTraits":"""
            I'm convinced people are always trying to steal my secrets.
        """,
        "flaws":"""
            I overlook obvious solutions in favor of more complicated ones.
        """,
        "ideals":"""
            Knowledge. The path to power and self-improvement is through knowledge.
        """,
        "bonds":"""
            I have an ancient text that holds awesome secrets. I must study it and learn what it has to teach me.
        """
    }

    return character