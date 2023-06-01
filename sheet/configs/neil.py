id = 1

def apply(character):
    character.id = id
    character.config = {"edition":"Pathfinder", "critType":'doubleAll', "castingType":"vancian"}
    character.name = "Nail"
    character.baseStats = '14,16,14,12,16,8'
    character.alignment = "Chaotic Neutral"
    character.charClass = {"name":"Warpriest", "options":{}}
    character.level = 4
    character.background = {'name':"In Their Footsteps"}
    character.feats = {"Two-Weapon Fighting":"Level 1:", "Butterfly Sting":"Level 3", "Combat Reflexes":"Warpriest 3 Bonus Feat"}
    character.race = {"name":"Half-Orc", "options":{"primaryAbility":"Dexterity", "secondaryAbility":"None", "languages":["Draconic"]}}
    character.playerName = "Griffin"
    character.traits = ["Fate's Favored", "Anatomist"]
    character.weapon = [
        {"displayName":"+1 Kukri", "name" : "Kukri", "bonus":1, "damageDie" : "1d4", "critRange":"18-20", "critDamage":2, "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Strength' ,'tags':['TWF','Main']},
        {"displayName":"Kukri", "name" : "Kukri", "bonus":0, "damageDie" : "1d4", "critRange":"18-20", "critDamage":2, "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Strength','tags':['TWF','Off-Hand'] },
        {"displayName":"Chakram", "name" : "Chakram (30ft.)", "bonus":0, "damageDie" : "1d8", "critRange":"20", "critDamage":2, "damageType": "S", "toHitAbility": "Dexterity", "damageAbility": 'Strength', 'tags':['ranged']},
    ]
    character.equipment = {
        "head"     : {"name":""},
        "headband" : {"name":""},
        "eyes"     : {"name":""},
        "shoulders": {"name":""},
        "neck"     : {"name":""},
        "chest"    : {"name":""},
        "body"     : {"name":"Quick Runners Shirt"},
        "armor"    : {"name":"Chain Shirt", "armorBonus" : 4, "ability":"Dex", "maxAbility": 4, "armorCheck" : 2, "spellFailure" : 20, "modifiers": []},
        "belt"     : {"name":""},
        "wrists"   : {"name":""},
        "hands"    : {"name":""},
        "ring1"    : {"name":""},
        "ring2"    : {"name":""},
        "feet"     : {"name":""},
    }
    character.skillRanks = {
        'Heal'                 : 1,
        'Handle Animal'        : 1,
        'Knowledge - Religion' : 1,
        'Perception'           : 4,
        'Stealth'              : 4,
        'Survival'             : 1,
    }

    character.accentColor = ["skyblue", "white"]

    character.flavor = {
        "backstory":"""
            Neil's grandfather was an adventurer. When his grandfather cam e back from his escapades, he would regale Neil and his brother Tamir with the stories. His grandfather found many treasures throughout his years and passed a few along to his grandsons. He gifted Neil a sacred knife of the goddess Sheredin. Legend had it that the knife would protect the wielder and guide them to true freedom. 
            Eventually, their grandfather went out in search of the secret to immortality. He never came back. So the brothers set out to find their grandfather. Their best idea was to try and follow the path their grandfather had been following, the path to immortality. Of the two brothers, the idea of immortality intrigued Neil more than Tamir. Immortality was the ultimate freedom, the ability to live forever and pursue any goal you desired without the fear of running out of time.
            After searching for many years, their grandfathers trail has gone cold. They have not given up on finding him, but the goal has ended up slipping down their list of priorities as time has gone on.
        """,
        "personalityTraits":"""
            Blessed by Sheredin with good looks but not the personality to use them
        """,
        "flaws":"""
            I do not think before I act.
            Sometimes I trust my goddess too much to guide me
        """,
        "ideals":"""
            I will search for freedom in whatever forms I can.
            The ultimate freedom is immortality
        """,
        "bonds":"""
            Devoted to his goddess, Sheredin
            Fiercly loyal to his brother, Tamir
        """
    }

    return character