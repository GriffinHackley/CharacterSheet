from sheet.modifiers import Modifier


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
        self.defaultToggles = {}
        self.defaultToggles["Critical"] = Toggle(
            "Critical",
            "",
            [],
        )
        self.defaultToggles["Advantage"] = Toggle(
            "Advantage",
            "",
            [],
        )

    def addToggle(self, toggle: Toggle):
        self.list[toggle.name] = toggle

    def addToggleList(self, toggleList):
        self.list = self.list | toggleList.list

    def isInList(self, name):
        if name in self.list.keys():
            return True

        if name in self.defaultToggles.keys():
            return True

        return False

    def getFullList(self):
        ret = {}

        ret.update(self.list)
        ret.update(self.defaultToggles)

        return ret

    def toJson(self):
        ret = {}
        ret["other"] = {}
        ret["default"] = {}

        for toggle, data in self.list.items():
            ret["other"][toggle] = data.isUsed

        for toggle, data in self.defaultToggles.items():
            ret["default"][toggle] = data.isUsed

        ret["other"] = dict(sorted(ret["other"].items()))
        ret["default"] = dict(sorted(ret["default"].items()))

        return ret

    def addSpellToggles(self, spellList):
        spellEffects = spellList.getToggleList()
