import math
from ..modifiers import Modifier, ModifierList
from .. import classes

def allClasses():
    module = __import__("sheet")
    module = getattr(module, "classes")

    ret = {}
    for character in classes.__all__:
        current = getattr(module, character)
        ret[character] = current

    return ret

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
        proficiencyList['armor'] = proficiencyList['armor'] + self.proficiencies['armor']
        proficiencyList['weapons'] = proficiencyList['weapons'] + self.proficiencies['weapons']
        proficiencyList['languages'] = proficiencyList['languages'] + self.proficiencies['languages']
        if self.edition == "5e":
            proficiencyList['skills'] = proficiencyList['skills'] + self.proficiencies['skills']
            proficiencyList['tools'] = proficiencyList['tools'] + self.proficiencies['tools']
            proficiencyList['savingThrows'] = proficiencyList['savingThrows'] + self.proficiencies['savingThrows']