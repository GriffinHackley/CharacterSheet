from .races import Race
from ..modifiers import Modifier, ModifierList
from ..static.addParagraphTags import addParagraphTags


class AstralElf(Race):
    def setLevel(self, level):
        return super().setLevel(level)

    def setOptions(self, options):
        options["languages"] = options["languages"]
        options["tools"] = ["tool1", "tool2"]
        return super().setOptions(options)

    def __init__(self):
        self.name = "Astral Elf"
        self.skills = ["Perception"]
        super().__init__()

    def appendModifiers(self, modList: ModifierList):
        return super().appendModifiers(modList)

    def getFeatures(self):
        ret = super().getFeatures(
            darkvision=True,
            creatureType="You are a Humanoid. You are also considered an elf for any prerequisite or effect that requires you to be an elf.",
        )

        toAdd = [
            {
                "name": "Astral Fire",
                "text": "You know the Sacred Flame cantrip. Intelligence is your spellcasting ability for it",
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
                "name": "Starlight Step",
                "text": "As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.",
            },
            {
                "name": "Trance",
                "text": "You don't need to sleep, and magic can't put you to sleep. You can finish a long rest in 4 hours if you spend those hours in a trancelike meditation, during which you remain conscious. Whenever you finish this trance, you gain proficiency in one skill of your choice and with one weapon or tool of your choice, selected from the Player's Handbook. You magically acquire these proficiencies by drawing them from shared elven memory and the experiences of entities on the Astral Plane, and you retain them until you finish your next long rest.",
            },
        ]

        for current in toAdd:
            current["text"] = addParagraphTags(current["text"])

        return ret + toAdd
