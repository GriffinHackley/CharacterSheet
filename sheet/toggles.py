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

    def addToggle(self, toggle: Toggle):
        self.list[toggle.name] = toggle

    def toJson(self):
        ret = {}

        for toggle, data in self.list.items():
            ret[toggle] = data.isUsed

        return ret

    def masterList(self):
        masterList = []

        return masterList

    # def addSpellToggles(self):
    #     self.list.append(
    #         Toggle(
    #             "Absorb Elements",
    #             "spell",
    #             [Modifier("1d6", "elemental", "Melee-DamageDie", "Absorb Elements")],
    #         )
    #     )

    #     self.list.append(
    #         Toggle(
    #             "Booming Blade",
    #             "spell",
    #             [Modifier("0d8", "untyped", "DamageDie", "Booming Blade")],
    #         )
    #     )

    #     self.list.append(
    #         Toggle(
    #             "Cats Grace",
    #             "spell",
    #             [Modifier(4, "enhancement", "Dexterity", "Cats Grace")],
    #         )
    #     )

    #     self.list.append(
    #         Toggle(
    #             "Divine Favor",
    #             "spell",
    #             [
    #                 Modifier(1, "luck", "ToHit", "Divine Favor"),
    #                 Modifier(1, "luck", "Damage", "Divine Favor"),
    #             ],
    #         )
    #     )

    #     self.list.append(
    #         Toggle(
    #             "Favored Foe",
    #             "spell",
    #             [Modifier("1d4", "untyped", "DamageDie", "Favored Foe")],
    #         )
    #     )

    #     self.list.append(
    #         Toggle(
    #             "Hunter's Mark",
    #             "spell",
    #             [Modifier("1d6", "untyped", "DamageDie", "Hunter's Mark")],
    #         )
    #     )

    #     self.list.append(
    #         Toggle(
    #             "Iron Skin",
    #             "spell",
    #             [Modifier(4, "enhancement", "Natural Armor", "Iron Skin")],
    #         )
    #     )

    #     self.list.append(
    #         Toggle("Shield", "spell", [Modifier(5, "untyped", "AC", "Shield (Spell)")])
    #     )

    #     self.list.append(
    #         Toggle(
    #             "Shield Of Faith",
    #             "spell",
    #             [Modifier(2, "deflection", "AC", "Shield of Faith")],
    #         )
    #     )
