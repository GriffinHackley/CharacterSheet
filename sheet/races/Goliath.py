from .races import Race
from ..modifiers import Modifier, ModifierList
from ..static.addParagraphTags import addParagraphTags


class Goliath(Race):
    def setOptions(self, options):
        options["languages"] = options["Giant"]
        return super().setOptions(options)

    def setLevel(self, level):
        return super().setLevel(level)

    def __init__(self):
        self.name = "Goliath"
        self.skills = ["Athletics"]
        super().__init__()

    def appendModifiers(self, modList: ModifierList):
        return super().appendModifiers(modList)

    def getFeatures(self):
        toAdd = [
            {
                "name": "Little Giant",
                "text": " You have proficiency in the Athletics skill, and you count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.",
            },
            {
                "name": "Mountain Born",
                "text": "You have resistance to cold damage. You also naturally acclimate to high altitudes, even if you’ve never been to one. This includes elevations above 20,000 feet.",
            },
            {
                "name": "Stone's Endurance",
                "text": addParagraphTags(
                    """
                    You can supernaturally draw on unyielding stone to shrug off harm. When you take damage, you can use your reaction to roll a d12. Add your Constitution modifier to the number rolled and reduce the damage by that total.
                    You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.
                    """
                ),
            },
        ]

        ret = super().getFeatures(toAdd)

        return ret
