from .races import Race
from ..modifiers import ModifierList
from ..static.addParagraphTags import addParagraphTags


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
        self.feat = {"____": {}}
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

        toAdd = [
            {
                "name": next(iter(self.feat)),
                "text": addParagraphTags(
                    """
                    You gain the {} feat. 
                    See the \"Feats\" section under the \"Misc.\" tab for more information
                    """.format(
                        next(iter(self.feat))
                    )
                ),
            }
        ]

        ret = super().getFeatures(toAdd, darkvision=darkvision)

        return ret
