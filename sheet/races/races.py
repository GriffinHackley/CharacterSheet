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
    name                = ''
    abilityDistribution = ''
    primaryAbility      = ''
    secondaryAbility    = ''
    size                = ''
    feat                = ''
    speed               = 0
    languages           = [] 
    skillBonus          = []
    features            = []
    classSkills         = []
    skills              = []
    tools               = []
    misc                = []

    def appendModifiers(self, modList:ModifierList):
        try:
            if self.abilityDistribution == "2/1":
                modList.addModifier(Modifier(2,"untyped", self.primaryAbility, self.name))
                modList.addModifier(Modifier(1,"untyped", self.secondaryAbility, self.name))
        
            if self.abilityDistribution == "2/0":
                modList.addModifier(Modifier(2,"untyped", self.primaryAbility, self.name))
                if self.secondaryAbility != '':
                    raise Exception()

            if self.abilityDistribution == "1/1":
                modList.addModifier(Modifier(1,"untyped", self.primaryAbility, self.name))
                modList.addModifier(Modifier(1,"untyped", self.secondaryAbility, self.name))
        
        except:
            error = "You chose an ability distribution of {}, but primaryAbility={} and secondaryAbility={}"
            raise Exception(error.format(self.abilityDistribution, self.primaryAbility, self.secondaryAbility))

        

    def addProficiencies(self, proficiencyList):
        #NOTE: skill proficiency is used in place of class skills for pf characters
        proficiencies = [{'skills': self.skills}, {'languages':self.languages}, {'tools': self.tools}]

        for proficiency in proficiencies:
            for key,value in proficiency.items():
                if not key in proficiencyList.keys():
                    raise Exception("Key '" + key + "' was found in proficiencies but does not exist")
                
                proficiencyList[key] = proficiencyList[key] + value

    def getConsumables(self, profBonus):
        return []
    
    def getFeat(self):
        if self.feat == '':
            return []
        self.feat['source'] = self.name
        
        return [self.feat]
    
    def getFeatures(self, darkvision=False, creatureType="You are humanoid", extraAttributes=[]):
        ret = []
        
        size = "You are {}".format(self.size)
        speed = "Your walking speed is {} feet.".format(self.speed)

        ret = ret + [{
            "name": "Attributes",
            "text": [
                {"type": "heading", "text":"Creature Type:"},
                {"type": "normal", "text":creatureType},

                {"type": "heading", "text":"Size:"},
                {"type": "normal", "text":size},

                {"type": "heading", "text":"Speed:"},
                {"type": "normal", "text":speed},
            ] + extraAttributes
        }] 

        if darkvision:
            ret = ret + [{
                "name": "Darkvision",
                "text": [
                    {"type": "normal", "text":"You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray."}
                ]
            }]

        languages = "You can speak, read, and write Common"
        if len(self.languages) == 1:
            languages = languages + " and {}".format(self.languages[0])
        if len(self.languages) > 1:
            for i in range(len(self.languages)-1):
                languages = languages + ", {}".format(self.languages[i])
            languages = languages + ", and {}".format(self.languages[len(self.languages)-1])

        ret = ret + [{
            "name": "Languages",
            "text": [
                {"type": "normal", "text":languages}
            ]
        }]

        return ret
    
    def __init__(self, options):
        for option, value in options.items():
            if hasattr(self, option):
                setattr(self, option ,value)
            else:
                raise Exception("A race option was found in the config that does not exist. Option:" + option)