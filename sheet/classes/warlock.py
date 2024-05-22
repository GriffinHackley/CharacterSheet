from sheet.toggles import Toggle, ToggleList
from .classes import FifthEditionClass, Subclass
from ..modifiers import Modifier, ModifierList


class Warlock(FifthEditionClass):
    subclass = "Otherworldly Patron"
    proficiencies = {
        "skills": ["Arcana", "Investigation", "Performance"],
        "languages": [],
        "armor": ["Light"],
        "weapons": ["Simple"],
        "tools": [],
        "savingThrows": ["Charisma", "Wisdom"],
    }
    expertise = {"skills": []}

    def __init__(self):
        super().__init__(
            name="Warlock",
            hitDie="8",
            spellProgression="full",
            primaryStat="Charisma",
        )

    class Fiend(Subclass):
        i = 0
