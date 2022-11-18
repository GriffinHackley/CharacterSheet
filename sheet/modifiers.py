class Modifier():
    stat  = ''
    type  = ''
    bonus = 0

    def __init__(self, bonus, type, stat, source):
        self.bonus  = bonus
        self.type   = type
        self.stat   = stat
        self.source = source

    def __str__(self):
        return f"+{self.bonus} {self.type} bonus to {self.stat}"

class ModifierList():
    list = {}

    def __init__(self):
        self.list = {}

    def addModifier(self, modifier:Modifier):
        if not modifier.stat in self.list:
            self.list[modifier.stat] = []
        
        self.list[modifier.stat].append(modifier)

    def cleanModifiers(self, stats, profBonus):
        # Search through modlist and find any bonus that is not already an int
        for modifier in self.list:
            for bonus in self.list[modifier]:
                if not type(bonus.bonus) == int:
                    if bonus.bonus in stats:
                        bonus.bonus = stats[bonus.bonus]
                    if bonus.bonus == "Proficiency Bonus":
                        bonus.bonus = profBonus
    
    def applyModifier(self, modifierName):
        if (not modifierName in self.list):
            return 0
        allBonus = self.list[modifierName]
        total = 0
        for bonus in allBonus:
            total += bonus.bonus
        
        return total

    def applyModifierToModifier(self, modifier):
        for key,value in self.list.items():
            for mod in value:
                if mod.type == modifier.stat:
                    mod.bonus += modifier.bonus

    def getDieModifier(self, tags):
        modifierName = 'DamageDie'

        modifierList = []
        modifierList.append(modifierName)

        #Add all applicable tags to list of tags to apply
        if 'Ranged' in tags:
            modifierList.append('Ranged-'+modifierName)
        elif 'Melee' in tags:
            modifierList.append('Melee-'+modifierName)
        
        if 'Main' in tags:
            modifierList.append('Main-'+modifierName)
        elif 'Off-Hand' in tags:
            modifierList.append('Off-Hand-'+modifierName)

        #Add all applicable bonus' to list
        allBonus = []
        for modifier in modifierList:
            if modifier in self.list:
                allBonus = allBonus + self.list[modifier]

        #Group bonuses by die size
        die = {}
        for bonus in allBonus:
            temp = []
            [number,size] = bonus.bonus.split('d')
            temp.append(int(number))

            if size in die.keys():
                die[size] = die[size] + temp
            else:
                die[size] = temp
        
        #Add all values per die size
        for size,numbers in die.items():
            die[size] = sum(numbers)
        
        return die
    
    def applyModifierWithFilters(self, modifierName, filters):
        if (not modifierName in self.list):
            return 0
        allBonus = self.list[modifierName]
        total = 0
        for bonus in allBonus:
            if not bonus.type in filters:    
                total += bonus.bonus
        
        return total

