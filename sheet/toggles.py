from sheet.modifiers import Modifier


class Toggle:
    def __init__(self, name, type, modifiers):
        self.name = name
        self.type = type
        self.modifiers = modifiers

    def __str__(self):
        return f"+{self.bonus} {self.type} bonus to {self.stat}"


class ToggleList:
    def __init__(self):
        self.list = []

    def addToggle(self, toggle: Toggle):
        self.list.append(toggle)

    def masterList(self):
        masterList = []

        masterList += self.addSpellToggles(masterList)

        return masterList

    def addSpellToggles(self, masterList):
        masterList.append(
            Toggle(
                "Absorb Elements",
                "spell",
                [Modifier("1d6", "elemental", "Melee-DamageDie", "Absorb Elements")],
            )
        )

        masterList.append(
            Toggle(
                "Booming Blade",
                "spell",
                [Modifier("0d8", "untyped", "DamageDie", "Booming Blade")],
            )
        )

        masterList.append(
            Toggle(
                "Cats Grace",
                "spell",
                [Modifier(4, "enhancement", "Dexterity", "Cats Grace")],
            )
        )

        masterList.append(
            Toggle(
                "Divine Favor",
                "spell",
                [
                    Modifier(1, "luck", "ToHit", "Divine Favor"),
                    Modifier(1, "luck", "Damage", "Divine Favor"),
                ],
            )
        )

        masterList.append(
            Toggle(
                "Favored Foe",
                "spell",
                [Modifier("1d4", "untyped", "DamageDie", "Favored Foe")],
            )
        )

        masterList.append(
            Toggle(
                "Hunter's Mark",
                "spell",
                [Modifier("1d6", "untyped", "DamageDie", "Hunter's Mark")],
            )
        )

        masterList.append(
            Toggle(
                "Iron Skin",
                "spell",
                [Modifier(4, "enhancement", "Natural Armor", "Iron Skin")],
            )
        )

        masterList.append(
            Toggle("Shield", "spell", [Modifier(5, "untyped", "AC", "Shield (Spell)")])
        )

        masterList.append(
            Toggle(
                "Shield Of Faith",
                "spell",
                [Modifier(2, "deflection", "AC", "Shield of Faith")],
            )
        )

        return masterList
