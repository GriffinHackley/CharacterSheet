import json
from .races import races

from sheet.misc.backgrounds import FifthEditionBackground


class Plan:
    def getPlan(self, character):
        self.character = character
        ret = []

        ret.append(self.getLevelZeroPlan())

        return json.dumps(ret)

    def getLevelZeroPlan(self):
        ret = {}

        # Get all backgrounds
        ret["background"] = FifthEditionBackground.getAllFeatures()

        # Get all races

        return ret
