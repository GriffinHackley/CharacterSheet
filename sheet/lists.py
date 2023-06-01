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
    "Acrobatics"                : {"ability":"Dex", "acp":True , },
    "Appraise"                  : {"ability":"Int", "acp":False, },
    "Bluff"                     : {"ability":"Cha", "acp":False, },
    "Climb"                     : {"ability":"Str", "acp":True , },
    "Craft"                     : {"ability":"Int", "acp":False, },
    "Diplomacy"                 : {"ability":"Cha", "acp":False, },
    "Disable Device"            : {"ability":"Dex", "acp":True , },
    "Disguise"                  : {"ability":"Cha", "acp":False, },
    "Escape Artist"             : {"ability":"Dex", "acp":True , },
    "Fly"                       : {"ability":"Dex", "acp":True , },
    "Handle Animal"             : {"ability":"Wis", "acp":False, },
    "Heal"                      : {"ability":"Wis", "acp":False, },
    "Intimidate"                : {"ability":"Cha", "acp":False, },
    "Linguistics"               : {"ability":"Int", "acp":False, },
    "Perception"                : {"ability":"Wis", "acp":False, },
    "Perform"                   : {"ability":"Cha", "acp":False, },
    "Profession"                : {"ability":"Wis", "acp":False, },
    "Ride"                      : {"ability":"Dex", "acp":True , },
    "Sense Motive"              : {"ability":"Wis", "acp":False, },
    "Sleight of Hand"           : {"ability":"Dex", "acp":True , },
    "Spellcraft"                : {"ability":"Int", "acp":False, },
    "Stealth"                   : {"ability":"Dex", "acp":True , },
    "Survival"                  : {"ability":"Wis", "acp":False, },
    "Swim"                      : {"ability":"Str", "acp":True , },
    "Use Magic Device"          : {"ability":"Cha", "acp":False, },
    
    "Knowledge - Arcana"        : {"ability":"Int", "acp":False, },
    "Knowledge - Dungeoneering" : {"ability":"Int", "acp":False, },
    "Knowledge - Engineering"   : {"ability":"Int", "acp":False, },
    "Knowledge - Geography"     : {"ability":"Int", "acp":False, },
    "Knowledge - History"       : {"ability":"Int", "acp":False, },
    "Knowledge - Local"         : {"ability":"Int", "acp":False, },
    "Knowledge - Nature"        : {"ability":"Int", "acp":False, },
    "Knowledge - Nobility"      : {"ability":"Int", "acp":False, },
    "Knowledge - Planes"        : {"ability":"Int", "acp":False, },
    "Knowledge - Religion"      : {"ability":"Int", "acp":False, },
}
knowledge_skills_pathfinder =  [
    
]
skill_list_5e = {
    "Acrobatics"      : {"ability":"Dex"},
    "Animal Handling" : {"ability":"Wis"},
    "Arcana"          : {"ability":"Int"},
    "Athletics"       : {"ability":"Str"},
    "Deception"       : {"ability":"Cha"},
    "History"         : {"ability":"Int"},
    "Insight"         : {"ability":"Wis"},
    "Intimidation"    : {"ability":"Cha"},
    "Investigation"   : {"ability":"Int"},
    "Medicine"        : {"ability":"Wis"},
    "Nature"          : {"ability":"Int"},
    "Perception"      : {"ability":"Wis"},
    "Performance"     : {"ability":"Cha"},
    "Persuasion"      : {"ability":"Cha"},
    "Religion"        : {"ability":"Int"},
    "Sleight of Hand" : {"ability":"Dex"},
    "Stealth"         : {"ability":"Dex"},
    "Survival"        : {"ability":"Wis"},
}

save_list_pathfinder = {
    "Fortitude" : {"ability":"Con"},
    "Reflex"    : {"ability":"Dex"},
    "Will"      : {"ability":"Wis"},
}

combat_list = {
    "AC"            : {"ability":"Dex"},
    "Initiative"    : {"ability":"Dex"},
    "Speed"         : {"ability":"N/A"},
    "HP"            : {"ability":"Con"},
    "Hit Dice"      : {"ability":"N/A"},
}