from .races import Race
from ..modifiers import Modifier, ModifierList

class CustomLineage(Race):
    def __init__(self, options):
        options['name'] = "Custom Lineage"
        options['size'] = options['size']
        options['speed'] = 30
        options['languages'] = ["Common"]
        super().__init__(options)

    def appendModifiers(self, modList: ModifierList):
        return super().appendModifiers(modList)

    def getFeatures(self):
        creatureType = "You are a humanoid. You have the appearance of an Emerald Dragonborn."
        ret = super().getFeatures(creatureType=creatureType)

        ret['Languages'] = [
            {"type": "normal", "text":"You can speak, read, and write Common and ___IDK___"}
        ]

        return ret
