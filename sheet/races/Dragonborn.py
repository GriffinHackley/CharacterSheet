from .races import Race
from ..modifiers import Modifier, ModifierList


class Dragonborn(Race):
    def setOptions(self, options):
        options["name"] = "Dragonborn"
        options["skills"] = []
        options["languages"] = options["languages"]
        return super().setOptions(options)

    def __init__(self):
        self.name = "Dragonborn"
        super().__init__()

    def appendModifiers(self, modList: ModifierList):
        return super().appendModifiers(modList)

    def getConsumables(self, abilityScores, profBonus):
        ret = {}

        ret["Breath Weapon"] = BreathWeapon(
            profBonus, abilityScores["Constitution"], self.level
        ).toJson()

        return ret

    def getFeatures(self):
        extraAttributes = []

        ret = super().getFeatures(extraAttributes=extraAttributes)

        ret = ret + []

        return ret


class BreathWeapon:
    def __init__(self, profBonus, conMod, level):
        self.uses = profBonus
        self.dc = 8 + profBonus + conMod
        self.areaType = "15-ft cone"
        self.damage = self.getDamage(level)

    def getDamage(self, level):
        if level < 5:
            return "1d10"

        if level >= 5 and level < 10:
            return "2d10"

        if level >= 11 and level < 16:
            return "3d10"

        if level >= 17:
            return "4d10"

        raise Exception(
            "The level given for breath weapon was not valid: {}".format(level)
        )

    def toJson(self):
        return {"uses": self.uses}
