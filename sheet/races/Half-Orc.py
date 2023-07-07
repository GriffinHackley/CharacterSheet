from .races import Race
from ..modifiers import Modifier, ModifierList


class HalfOrc(Race):
    def __init__(self, options):
        options["name"] = "Half-Orc"
        options["size"] = "M"
        options["speed"] = 30
        options["languages"] = ["Common", "Orc"] + options["languages"]
        options["skills"] = ["Stealth", "Perception"]

        super().__init__(options)

    def appendModifiers(self, modList: ModifierList):
        modList.addModifier(Modifier(1, "luck", "Fortitude", "Sacred Tattoo"))
        modList.addModifier(Modifier(1, "luck", "Reflex", "Sacred Tattoo"))
        modList.addModifier(Modifier(1, "luck", "Will", "Sacred Tattoo"))

        for mod in self.skillBonus:
            modList.addModifier(mod)

        return super().appendModifiers(modList)

    def getFeatures(self):
        ret = {}

        # TODO: Use general race thing for pathfinder character as well
        ret["Attributes"] = [
            {"type": "heading", "text": "Creature Type:"},
            {
                "type": "normal",
                "text": "Half-orcs are Humanoid creatures with both the human and orc subtypes.",
            },
            {"type": "heading", "text": "Size:"},
            {
                "type": "normal",
                "text": "Half-orcs are Medium creatures and thus have no bonuses or penalties due to their size.",
            },
            {"type": "heading", "text": "Base Speed:"},
            {"type": "normal", "text": "Half-orcs have a base speed of 30 feet."},
        ]

        ret["Scavenger"] = [
            {
                "type": "normal",
                "text": "Some half-orcs eke out a leaving picking over the garbage heaps of society, and must learn to separate rare finds from the inevitable dross. Half-orcs with this racial trait receive a +2 racial bonus on Appraise checks and on Perception checks to find hidden objects (including traps and secret doors), determine whether food is spoiled, or identify a potion by taste. This racial trait replaces the intimidating trait.",
            },
        ]

        ret["Sacred Tattoo"] = [
            {
                "type": "normal",
                "text": "Many half-orcs decorate themselves with tattoos, piercings, and ritual scarification, which they consider sacred markings. Half-orcs with this racial trait gain a +1 luck bonus on all saving throws. This racial trait replaces orc ferocity.",
            },
        ]

        ret["Fey Thoughts"] = [
            {
                "type": "normal",
                "text": "Stealth and Perception are always class skills you. ",
            },
        ]

        ret["Darkvision"] = [
            {"type": "normal", "text": "Half-orcs can see in the dark up to 60 feet."},
        ]

        ret["Orc Blood"] = [
            {
                "type": "normal",
                "text": "Half-orcs count as both humans and orcs for any effect related to race.",
            },
        ]

        ret["Languages"] = [
            {
                "type": "normal",
                "text": "Half-orcs begin play speaking Common and Orc. You also know [One other language] due to high intelligence",
            },
        ]

        return ret
