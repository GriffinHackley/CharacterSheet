id = 4

def apply(character):
    character.id = id
    character.config = {"edition":"5e", "critType":'doubleDice',"castingType":"ritual"}
    character.name = "Ezekiel"
    character.baseStats = '10,15,12,12,13,15'
    character.alignment = "Lawful Neutral"
    character.charClass = {"name":"Rogue", "options":{}}
    character.level = 2
    character.background = {'name':"Spirit Medium", 'feature':'Spirit Medium'}
    character.feats = {}
    character.race = {"name":"Custom Lineage", "options":{"abilityDistribution":"1/1","primaryAbility":"Dexterity","secondaryAbility":"Charisma", "size":"Small", "feat":"Ritual Caster", "languages":[], "misc":{'variable trait':'darkvision'}}}
    character.playerName = "Griffin"
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

    character.accentColor = ["cornflowerblue", "yellow"]

    character.flavor = {
        "backstory":"""
            Temp
        """,
        "personalityTraits":"""
            Temp
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