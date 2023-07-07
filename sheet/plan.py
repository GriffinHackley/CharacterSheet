import json

from sheet.misc.backgrounds import FifthEditionBackground


class Plan:
    def getPlan(self, character):
        self.character = character
        ret = []

        ret.append(self.getLevelZeroPlan())

        return json.dumps(ret)

    def getLevelZeroPlan(self):
        background = FifthEditionBackground(self.character.background).toDict()

        ret = {}

        ret["Background"] = background

        return ret
