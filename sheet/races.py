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

    def getFeatures(self):
        ret = {}
        
        return ret

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

    def getFeatures(self):
        ret = {}

        ret['Attributes'] = [
{"type": "heading", "text":"""
Creature Type:
"""},
{"type": "normal", "text":"""
You are a Humanoid. You are also considered an elf for any prerequisite or effect that requires you to be an elf.
"""},
{"type": "heading", "text":"""
Size:
"""},
{"type": "normal", "text":"""
You are Medium
"""},
{"type": "heading", "text":"""
Speed:
"""},
{"type": "normal", "text":"""
Your walking speed is 30 feet.
"""},
]

        ret['Blessing of the Raven Queen'] = [
{"type": "normal", "text":"""
As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. 

Starting at 3rd level, you also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent.
"""}]

        ret['Darkvision'] = [
{"type": "normal", "text":"""
You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.
"""}]

        ret['Fey Ancestry'] = [
{"type": "normal", "text":"""
You have advantage on saving throws you make to avoid or end the charmed condition on yourself.
"""}]

        ret['Keen Senses'] = [
{"type": "normal", "text":"""
You have proficiency in the Perception skill.
"""}]

        ret['Necrotic Resistance'] = [
{"type": "normal", "text":"""
You have resistance to necrotic damage.
"""}]

        ret['Trance'] = [
{"type": "normal", "text":"""
You don’t need to sleep, and magic can’t put you to sleep. You can finish a long rest in 4 hours if you spend those hours in a trancelike meditation, during which you retain consciousness. 

Whenever you finish this trance, you can gain two proficiencies that you don’t have, each one with a weapon or a tool of your choice selected from the Player’s Handbook. You mystically acquire these proficiencies by drawing them from shared elven memory, and you retain them until you finish your next long rest.
"""}]

        ret['Languages'] = [
{"type": "normal", "text":"""
Your character can speak, read, and write Common and Elven
"""}]

        return ret

races = {}
races['Half-Orc'] = HalfOrc(primaryAbility="Dexterity", secondaryAbility="None", languages=[])
races['Shadar-Kai'] = ShadarKai(primaryAbility="Dexterity", secondaryAbility="Wisdom", languages="Elven")