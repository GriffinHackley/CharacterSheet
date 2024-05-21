import math
import re
from rest_framework.exceptions import APIException


class Modifier:
    stat = ""
    type = ""
    bonus = 0

    def __init__(self, bonus, stat, source=None, type="untyped"):
        self.bonus = bonus
        self.type = type
        self.stat = stat
        self.source = source

    def __str__(self):
        return f"+{self.bonus} {self.type} bonus to {self.stat}"


class ModifierList:
    list = {}

    def __init__(self):
        self.list = {}

    def addModifier(self, modifier: Modifier):
        if not modifier.stat in self.list:
            self.list[modifier.stat] = []

        if not modifier.source:
            raise APIException("Modifier has no source set")

        self.list[modifier.stat].append(modifier)

    def addModifierList(self, list):
        for mod in list:
            self.addModifier(mod)

    def cleanModifiers(self, stats, profBonus):
        # Search through modlist and find any bonus that is not already an int
        for modifier in self.list:
            for bonus in self.list[modifier]:
                if not type(bonus.bonus) == int:
                    if bonus.bonus in stats:
                        bonus.bonus = stats[bonus.bonus]
                    if bonus.bonus == "Proficiency Bonus":
                        bonus.bonus = profBonus
                    if bonus.bonus == "Proficiency/2":
                        bonus.bonus = math.floor(profBonus / 2)

    def applyModifier(self, modifierName):
        if not modifierName in self.list:
            return (0, {})

        allBonus = self.list[modifierName]
        total = 0
        source = {}
        for bonus in allBonus:
            if not type(bonus.bonus) == int:
                raise APIException(
                    "The type of bonus for {} is not an int".format(bonus.source)
                )
            source[bonus.source] = bonus.bonus
            total += bonus.bonus

        return (total, source)

    def applyDieModifier(self, modifierName, originalDamage):
        die = {}
        [number, size] = originalDamage.split("d")
        die[size] = [int(number)]

        source = {"Base": originalDamage}

        if not modifierName in self.list:
            return (originalDamage, source)

        allBonus = self.list[modifierName]
        pattern = re.compile("([1-9]+d[1-9])")

        for bonus in allBonus:
            temp = []
            if pattern.match(bonus.bonus):
                [number, size] = bonus.bonus.split("d")
            else:
                raise APIException("Invalid die type:{}".format(bonus.bonus))

            temp.append(int(number))

            source[bonus.source] = bonus.bonus

            if size in die.keys():
                die[size] = die[size] + temp
            else:
                die[size] = temp

        # Add all values per die size
        for size, numbers in die.items():
            die[size] = sum(numbers)

        return (die, source)

    def applyModifierToModifier(self, modifier):
        for key, value in self.list.items():
            for mod in value:
                if mod.type == modifier.stat:
                    mod.bonus += modifier.bonus

    def getDieModifier(self, tags, spells):
        modifierName = "DamageDie"

        modifierList = []
        modifierList.append(modifierName)

        # Add all applicable tags to list of tags to apply
        if "Ranged" in tags:
            modifierList.append("Ranged-" + modifierName)
        elif "Melee" in tags:
            modifierList.append("Melee-" + modifierName)

        if "Main" in tags:
            modifierList.append("Main-" + modifierName)
        elif "Off-Hand" in tags:
            modifierList.append("Off-Hand-" + modifierName)

        # Add all applicable bonus' to list
        allBonus = []
        for modifier in modifierList:
            if modifier in self.list:
                allBonus = allBonus + self.list[modifier]

        # Group bonuses by die size
        die = {}
        source = {}
        for bonus in allBonus:
            bonusDie = {}
            pattern = re.compile("([1-9]+d[1-9])")
            if pattern.match(bonus.bonus):
                [number, size] = bonus.bonus.split("d")
                bonusDie = {size: number}
            elif bonus.bonus == "Spell Damage":
                spell = spells.findSpell(bonus.source)
                bonus.bonus = self.formatDice(spell.damage)
                bonusDie = spell.damage
            else:
                raise APIException("Invalid bonus type")

            source[bonus.source] = bonus.bonus

            for size, number in bonusDie.items():
                if size in die.keys():
                    die[size] = die[size] + [int(number)]
                else:
                    die[size] = [int(number)]

        # Add all values per die size
        for size, numbers in die.items():
            die[size] = sum(numbers)

        return (die, source)

    def formatDice(self, allDice):
        if len(allDice) == 1:
            return "{}d{}".format(list(allDice.values())[0], list(allDice.keys())[0])

        formatted = ""
        first = True
        for size, number in dict(reversed(sorted(allDice.items()))).items():
            if first:
                formatted = "[{}d{}".format(number, size)
                first = False
            else:
                formatted = formatted + " + {}d{}".format(number, size)
        formatted += "]"
        return formatted

    def applyModifierWithFilters(self, modifierName, filters):
        if not modifierName in self.list:
            return (0, {})

        allBonus = self.list[modifierName]
        total = 0
        source = {}
        for bonus in allBonus:
            if not bonus.type in filters:
                source[bonus.source] = bonus.bonus
                total += bonus.bonus

        return (total, source)
