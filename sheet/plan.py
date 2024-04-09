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
        ret["backgrounds"] = {"all": FifthEditionBackground.getAllFeatures()}

        # Get all races
        ret["races"] = {
            "all": races.allRacesDict(),
            "choice": self.character.race["name"],
        }

        ret["stats"] = {
            "base": self.character.baseStats,
            "racial": self.character.race["options"]["abilityScores"],
            "feats": self.character.feats,
        }

        return ret
