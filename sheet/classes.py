import math
from .modifiers import Modifier, ModifierList

class Class():
    def __init__(self, level, name, hitDie, edition, fort="poor", refl="poor", will="poor", bab="1/2"):
        self.edition = edition
        self.name = name
        self.hitDie = hitDie
        self.level = level
        if edition == "Pathfinder":
            self.fort = self.getSave(fort)
            self.refl = self.getSave(refl)
            self.will = self.getSave(will)
            self.bab = self.getBab(bab)
        print()
    
    def getBab(self, progression):
        if progression == "full":
            return self.level
        elif progression == "3/4":
            return math.floor(self.level*3/4)
        elif progression == "1/2":
            return math.floor(self.level/2)

    def getSave(self, progression):        
        if progression == "good":
            return 2+math.ceil((self.level-1)/2)
        elif progression == "poor":
            return math.floor((self.level)/3)

    def appendModifiers(self, modList:ModifierList):
        if self.edition == "Pathfinder":
            modList.addModifier(Modifier(self.bab ,"untyped", 'ToHit'    , self.name+' BAB'))
            modList.addModifier(Modifier(self.fort,"untyped", 'Fortitude', self.name+' Fortitude'))
            modList.addModifier(Modifier(self.refl,"untyped", 'Reflex'   , self.name+' Reflex'))
            modList.addModifier(Modifier(self.will,"untyped", 'Will'     , self.name+' Will'))
    
    def addProficiencies(self, proficiencyList):
        if self.edition == "5e":
            proficiencyList['skills'] = proficiencyList['skills'] + self.proficiencies['skills']
            proficiencyList['armor'] = proficiencyList['armor'] + self.proficiencies['armor']
            proficiencyList['weapons'] = proficiencyList['weapons'] + self.proficiencies['weapons']
            proficiencyList['tools'] = proficiencyList['tools'] + self.proficiencies['tools']
            proficiencyList['saving throws'] = proficiencyList['saving throws'] + self.proficiencies['saving throws']
    
class Warpiest(Class):    
    skillPerLevel = 2
    sacredWeapon  = ''
    classSkills   = ['Climb', 'Craft', 'Diplomacy', 'Handle Animal', 'Heal', 'Intimidate', 'Knowledge (Engineering)', 
                     'Knowledge(Religion)', 'Profession', 'Ride', 'Sense Motive', 'Spellcraft', 'Survival', 'Swim']

    def __init__(self, level):
        super().__init__(level, 'Warpriest', hitDie='8', edition="Pathfinder", bab="3/4", fort="good", refl="poor", will="good")
        self.sacredWeapon = self.getSacredWeapon()
    
    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

        modList.addModifier(Modifier(1,"untyped", 'ToHit-Kukri', 'Weapon Focus (Kukri)'))
    
    def getSacredWeapon(self):
        return '1d6'
    
    def getConsumables(self, stats):
        ret = {}
        ret['Blessings'] = 3 + math.floor(stats['Wisdom']/2)
        
        if self.level >= 2:
            ret['Fervor'] = 3 + math.floor(self.level/2)
        
        if self.level >= 4:
            ret['Focus Weapon'] = self.level

        return ret

class Ranger(Class):
    proficiencies = {'skills': ['Insight', 'Stealth', 'Survival'], 'armor': ['Light', 'Medium'], 'weapons':['Simple', 'Martial'], 'tools':[], 'saving throws':['Strength', 'Dexterity']}
    expertise = {'skills': ['Stealth']}

    def __init__(self, level):
        super().__init__(level, name="Ranger", hitDie='10', edition="5e")
    
    def appendModifiers(self, modList: ModifierList):
        super().appendModifiers(modList)

        modList.addModifier(Modifier(2,"untyped", 'ToHit-Ranged', 'Archery Fighting Style'))
        modList.addModifier(Modifier('Wisdom',"untyped", 'Initiative', 'Gloomstalker - Dread Ambusher'))

    def getClassFeatures(self):
        pass

    def getConsumables(self, stats, proficiencyBonus):
        huntersMark = stats['Wisdom']
        favoredFoe = proficiencyBonus
        return {'Favored Foe': favoredFoe, 'Hunters Mark': huntersMark}

classes = {}
classes['Warpriest'] = Warpiest(4)
classes['Ranger']    = Ranger(4)