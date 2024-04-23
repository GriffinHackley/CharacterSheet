from .races import Race
from ..modifiers import Modifier, ModifierList
from ..static.addParagraphTags import addParagraphTags


class ShadarKai(Race):
    def setOptions(self, options):
        options["languages"] = options["languages"]
        options["skills"] = ["Perception"]
        options["tools"] = ["tool1", "tool2"]
        return super().setOptions(options)

    def setLevel(self, level):
        return super().setLevel(level)

    def __init__(self):
        self.name = "Shadar-Kai"
        super().__init__()

    def appendModifiers(self, modList: ModifierList):
        return super().appendModifiers(modList)

    def getFeatures(self):
        ret = super().getFeatures(darkvision=True)

        toAdd = [
            {
                "name": "Blessing of the Raven Queen",
                "text": """
                As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.
                Starting at 3rd level, you also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent.
                """,
            },
            {
                "name": "Fey Ancestry",
                "text": "You have advantage on saving throws you make to avoid or end the charmed condition on yourself.",
            },
            {
                "name": "Keen Senses",
                "text": "You have proficiency in the Perception skill.",
            },
            {
                "name": "Necrotic Resistance",
                "text": "You have resistance to necrotic damage.",
            },
            {
                "name": "Trance",
                "text": """
                You don’t need to sleep, and magic can’t put you to sleep. You can finish a long rest in 4 hours if you spend those hours in a trancelike meditation, during which you retain consciousness.
                Whenever you finish this trance, you can gain two proficiencies that you don’t have, each one with a weapon or a tool of your choice selected from the Player’s Handbook. You mystically acquire these proficiencies by drawing them from shared elven memory, and you retain them until you finish your next long rest.
                """,
            },
        ]

        for current in toAdd:
            current["text"] = addParagraphTags(current["text"])

        return ret + toAdd
