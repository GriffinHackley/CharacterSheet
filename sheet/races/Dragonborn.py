from .races import Race
from ..modifiers import Modifier, ModifierList


class Dragonborn(Race):
    def __init__(self, options, level):
        options["name"] = "Dragonborn"
        options["skills"] = []
        options["languages"] = options["languages"]
        super().__init__(options, level)

    def appendModifiers(self, modList: ModifierList):
        return super().appendModifiers(modList)

    def getConsumables(self, abilityScores, profBonus):
        ret = {}

        ret["Breath Weapon"] = BreathWeapon(
            profBonus, abilityScores["Constitution"], self.level
        ).toJson()

        return ret

    def getFeatures(self):
        extraAttributes = [
            {"type": "heading", "text": "Life Span:"},
            {
                "type": "normal",
                "text": "Harengons have a life span of about a century.",
            },
        ]

        ret = super().getFeatures(extraAttributes=extraAttributes)

        ret = ret + [
            {
                "name": "Hare Trigger",
                "text": [
                    {
                        "type": "normal",
                        "text": "You can add your proficiency bonus to your initiative rolls.",
                    }
                ],
            },
            {
                "name": "Leporine Senses",
                "text": [
                    {
                        "type": "normal",
                        "text": "You have proficiency in the Perception skill.",
                    }
                ],
            },
            {
                "name": "Lucky Footwork",
                "text": [
                    {
                        "type": "normal",
                        "text": "When you fail a Dexterity saving throw, you can use your reaction to roll a d4 and add it to the save, potentially turning the failure into a success. You can't use this reaction if you're prone or your speed is 0.",
                    }
                ],
            },
            {
                "name": "Rabbit Hop",
                "text": [
                    {
                        "type": "normal",
                        "text": "As a bonus action, you can jump a number of feet equal to five times your proficiency bonus, without provoking opportunity attacks. You can use this trait only if your speed is greater than 0. You can use it a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.",
                    }
                ],
            },
        ]

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
