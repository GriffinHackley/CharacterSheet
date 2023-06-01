from .races import Race
from ..modifiers import Modifier, ModifierList

class CustomLineage(Race):
    def __init__(self, options):
        options['name'] = "Custom Lineage"
        options['size'] = options['size']
        options['speed'] = 30
        options['languages'] = ["sylvan", "draconic"]
        super().__init__(options)

    def appendModifiers(self, modList: ModifierList):
        return super().appendModifiers(modList)

    def getFeatures(self):
        creatureType = "You are a humanoid. You have the appearance of an Emerald Dragonborn."

        darkvision = False
        if self.misc['variable trait'] == 'darkvision':
            darkvision = True
        elif 'proficiency' in self.misc['variable trait']:
            skill = self.misc['variable trait'].replace("proficiency(","").replace(")","")
            self.skills = self.skills + [skill]

        ret = super().getFeatures(creatureType=creatureType, darkvision=darkvision)

        ret['Feat'] = [
            {"type": "normal", "text":"You gain the {} feat".format(self.feat)}
        ]

        return ret
