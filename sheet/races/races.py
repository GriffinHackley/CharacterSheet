from .. import races
from ..modifiers import Modifier, ModifierList

def allRaces():
    module = __import__("sheet")
    module = getattr(module, "races")

    ret = {}
    for race in races.__all__:
        current = getattr(module, race)
        ret[race] = current

    return ret

class Race():
    name             = ''
    primaryAbility   = ''
    secondaryAbility = ''
    size             = ''
    speed            = 0
    languages        = [] 
    skillBonus       = []
    features         = []
    classSkills      = []
    skills           = []
    tools            = []

    def appendModifiers(self, modList:ModifierList):
        modList.addModifier(Modifier(2,"untyped", self.primaryAbility, self.name))
        
        if not self.secondaryAbility == "None":
            modList.addModifier(Modifier(1,"untyped", self.secondaryAbility, self.name))

    def addProficiencies(self, proficiencyList):
        #NOTE: skill proficiency is used in place of class skills for pf characters
        proficiencies = [{'skills': self.skills}, {'languages':self.languages}, {'tools': self.tools}]

        for proficiency in proficiencies:
            for key,value in proficiency.items():
                if not key in proficiencyList.keys():
                    raise Exception("Key '" + key + "' found in proficiencies that does not exist")
                
                proficiencyList[key] = proficiencyList[key] + value

    def getConsumables(self, profBonus):
        return {}
    
    def __init__(self, options):
        for option, value in options.items():
            if hasattr(self, option):
                setattr(self, option ,value)
            else:
                raise Exception("A race option was found in the config that does not exist. Option:" + option)