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
        background = FifthEditionBackground(self.character.background).toDict()
        race = races.getRace(self.character.race["name"])(
            self.character.race["options"]
        ).toDict()
        print(race)

        ret = {}

        ret["Background"] = background
        ret["Race"] = race

        return ret
