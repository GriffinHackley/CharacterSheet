from sheet.modifiers import Modifier
from typing import Type, TypeVar


class Toggle:
    def __init__(self, name, type, modifiers: list[Modifier], isUsed=False):
        self.name = name
        self.type = type
        self.modifiers = modifiers
        self.isUsed = isUsed

    def __str__(self):
        return f"+{self.bonus} {self.type} bonus to {self.stat}"


class ToggleList:
    def __init__(self):
        self.list = {}

    def addToggle(self, toggle: Toggle):
        self.list[toggle.name] = toggle

    def addToggleList(self, toggleList):
        self.list = self.list | toggleList.list

    def toJson(self):
        ret = {}

        for toggle, data in self.list.items():
            ret[toggle] = data.isUsed

        return ret

    def addSpellToggles(self, spellList):
        spellEffects = spellList.getToggleList()
