from .races import Race
from ..modifiers import ModifierList


class CustomLineage(Race):
    def setOptions(self, options):
        options["size"] = options["size"]
        options["speed"] = 30
        options["languages"] = options["languages"]
        return super().setOptions(options)

    def setLevel(self, level):
        return super().setLevel(level)

    def __init__(self):
        self.name = "Custom Lineage"
        super().__init__()

    def appendModifiers(self, modList: ModifierList):
        return super().appendModifiers(modList)

    def getFeatures(self):
        creatureType = (
            "You are a humanoid. You have the appearance of an Emerald Dragonborn."
        )

        darkvision = False
        # TODO: Fix this
        # if self.misc["variable trait"] == "darkvision":
        #     darkvision = True
        # elif "proficiency" in self.misc["variable trait"]:
        #     skill = self.misc["variable trait"]
        #     self.skills = self.skills + [skill]

        ret = super().getFeatures(creatureType=creatureType, darkvision=darkvision)

        # TODO: Fix this
        # ret = ret + [
        #     {
        #         "name": "Feat",
        #         "text": [
        #             {
        #                 "type": "normal",
        #                 "text": "You gain the {} feat".format(self.feat["name"]),
        #             }
        #         ],
        #     }
        # ]

        return ret
