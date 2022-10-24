from .modifiers import Modifier, ModifierList

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

    def appendModifiers(self, modList:ModifierList):
        modList.addModifier(Modifier(2,"untyped", self.primaryAbility, self.name))
        if not self.secondaryAbility == "None":
            modList.addModifier(Modifier(1,"untyped", self.secondaryAbility, self.name))

    def addProficiencies(self, proficiencyList):
        for proficiency in self.proficiencies:
            for key,value in proficiency.items():
                proficiencyList[key].append(value)
    
    def __init__(self, name, primaryAbility, secondaryAbility='None', size='M', speed=30, languages=[], features=[]):
        self.name             = name
        self.primaryAbility   = primaryAbility  
        self.secondaryAbility = secondaryAbility
        self.size             = size            
        self.speed            = speed           
        self.languages        = languages             
        self.features         = features        

class HalfOrc(Race):
    def __init__(self, primaryAbility, secondaryAbility='None', languages=[]):
        super().__init__(primaryAbility=primaryAbility, secondaryAbility=secondaryAbility, name="Half-Orc",  size='M', speed=30, languages=["Common", "Orc"], features=[{"darkvision":"Half-orcs can see in the dark up to 60 feet."}])

    def appendModifiers(self, modList: ModifierList):
        modList.addModifier(Modifier(1,"luck", 'Fortitude', 'Sacred Tattoo'))
        modList.addModifier(Modifier(1,"luck", 'Reflex', 'Sacred Tattoo'))
        modList.addModifier(Modifier(1,"luck", 'Will', 'Sacred Tattoo'))
        modList.addModifier(Modifier(2,"racial", 'Appraise', 'Scavenger'))

        self.classSkills = ['Stealth', 'Perception']
        
        for mod in self.skillBonus:
            modList.addModifier(mod)

        return super().appendModifiers(modList)

class ShadarKai(Race):
    def __init__(self, primaryAbility, secondaryAbility='None', size='M', speed=30, languages=[], features=[]):
        super().__init__(primaryAbility=primaryAbility, secondaryAbility=secondaryAbility, name="ShadarKai", size=size, speed=speed, languages=["Common", languages], features=[{"darkvision":"See in the dark up to 60 feet."}])
        self.proficiencies = []

    def appendModifiers(self, modList: ModifierList):
        return super().appendModifiers(modList)

    def addProficiencies(self, proficiencyList):
        self.proficiencies = []
        self.proficiencies = self.proficiencies + [{'skills': 'Perception'}, {'tools': 'test'}, {'tools': 'test'}]
        super().addProficiencies(proficiencyList)

races = {}
races['Half-Orc'] = HalfOrc(primaryAbility="Dexterity", secondaryAbility="None", languages=[])
races['Shadar-Kai'] = ShadarKai(primaryAbility="Dexterity", secondaryAbility="Wisdom", languages="Elven")