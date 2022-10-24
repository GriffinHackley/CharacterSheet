from enum import Enum

class Ability(Enum):
    Strength     = 0
    Dexterity    = 1
    Constitution = 2
    Intelligence = 3
    Wisdom       = 4
    Charisma     = 5

    Str = 0
    Dex = 1
    Con = 2
    Int = 3
    Wis = 4
    Cha = 5


skill_list_pathfinder = {
    "Acrobatics"       : {"ability":"Dex", "value":0, "class": False, "acp":True , "ranks": 0, "modifiers":[]},
    "Appraise"         : {"ability":"Int", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Bluff"            : {"ability":"Cha", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Climb"            : {"ability":"Str", "value":0, "class": False, "acp":True , "ranks": 0, "modifiers":[]},
    "Craft"            : {"ability":"Int", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Diplomacy"        : {"ability":"Cha", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Disable Device"   : {"ability":"Dex", "value":0, "class": False, "acp":True , "ranks": 0, "modifiers":[]},
    "Disguise"         : {"ability":"Cha", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Escape Artist"    : {"ability":"Dex", "value":0, "class": False, "acp":True , "ranks": 0, "modifiers":[]},
    "Fly"              : {"ability":"Dex", "value":0, "class": False, "acp":True , "ranks": 0, "modifiers":[]},
    "Handle Animal"    : {"ability":"Wis", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Heal"             : {"ability":"Wis", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Intimidate"       : {"ability":"Cha", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Knowledge"        : {"ability":"Int", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Linguistics"      : {"ability":"Int", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Perception"       : {"ability":"Wis", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Perform"          : {"ability":"Cha", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Profession"       : {"ability":"Wis", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Ride"             : {"ability":"Dex", "value":0, "class": False, "acp":True , "ranks": 0, "modifiers":[]},
    "Sense Motive"     : {"ability":"Wis", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Sleight of Hand"  : {"ability":"Dex", "value":0, "class": False, "acp":True , "ranks": 0, "modifiers":[]},
    "Spellcraft"       : {"ability":"Int", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Stealth"          : {"ability":"Dex", "value":0, "class": False, "acp":True , "ranks": 0, "modifiers":[]},
    "Survival"         : {"ability":"Wis", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
    "Swim"             : {"ability":"Str", "value":0, "class": False, "acp":True , "ranks": 0, "modifiers":[]},
    "Use Magic Device" : {"ability":"Cha", "value":0, "class": False, "acp":False, "ranks": 0, "modifiers":[]},
}

skill_list_5e = {
    "Acrobatics"      : {"ability":"Dex", "value":0, "proficient": False, "modifiers":[]},
    "Animal Handling" : {"ability":"Wis", "value":0, "proficient": False, "modifiers":[]},
    "Arcana"          : {"ability":"Int", "value":0, "proficient": False, "modifiers":[]},
    "Athletics"       : {"ability":"Str", "value":0, "proficient": False, "modifiers":[]},
    "Deception"       : {"ability":"Cha", "value":0, "proficient": False, "modifiers":[]},
    "History"         : {"ability":"Int", "value":0, "proficient": False, "modifiers":[]},
    "Insight"         : {"ability":"Wis", "value":0, "proficient": False, "modifiers":[]},
    "Intimidation"    : {"ability":"Cha", "value":0, "proficient": False, "modifiers":[]},
    "Investigation"   : {"ability":"Int", "value":0, "proficient": False, "modifiers":[]},
    "Medicine"        : {"ability":"Wis", "value":0, "proficient": False, "modifiers":[]},
    "Nature"          : {"ability":"Int", "value":0, "proficient": False, "modifiers":[]},
    "Perception"      : {"ability":"Wis", "value":0, "proficient": False, "modifiers":[]},
    "Performance"     : {"ability":"Cha", "value":0, "proficient": False, "modifiers":[]},
    "Persuasion"      : {"ability":"Cha", "value":0, "proficient": False, "modifiers":[]},
    "Religion"        : {"ability":"Int", "value":0, "proficient": False, "modifiers":[]},
    "Sleight of Hand" : {"ability":"Dex", "value":0, "proficient": False, "modifiers":[]},
    "Stealth"         : {"ability":"Dex", "value":0, "proficient": False, "modifiers":[]},
    "Survival"        : {"ability":"Wis", "value":0, "proficient": False, "modifiers":[]},
}

save_list_pathfinder = {
    "Fortitude" : {"ability":"Con", "value":0, "modifiers":[]},
    "Reflex"    : {"ability":"Dex", "value":0, "modifiers":[]},
    "Will"      : {"ability":"Wis", "value":0, "modifiers":[]},
}

combat_list = {
    "AC"            : {"ability":"Dex", "value":10, "modifiers":[]},
    "Initiative"    : {"ability":"Dex", "value":0, "modifiers":[]},
    "Speed"         : {"ability":"N/A", "value":30, "modifiers":[]},
    "HP"            : {"ability":"Con", "value":0, "modifiers":[]},
    "Hit Dice"      : {"ability":"N/A", "value":0, "modifiers":[]},
}