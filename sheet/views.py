from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib import admin

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models.FifthEditionCharacter import FifthEditionCharacter
from .models.PathfinderCharacter import PathfinderCharacter
from .models.Characters import Character
from .plan import Plan
import json
from .races import races

admin.site.register(Character)


@api_view(["GET"])
def listCharacters(request):
    character_list = Character.objects.order_by("name")

    list = {}

    for character in character_list:
        list[character.id] = character.name

    return Response(list)


@api_view(["GET"])
def getCharacter(request, characterId):
    character = get_object_or_404(Character, pk=characterId)
    config = json.loads(character.config)

    # TODO: Do this dynamically
    if config["edition"] == "5e":
        character = FifthEditionCharacter(character)
    elif config["edition"] == "Pathfinder":
        character = PathfinderCharacter(character)
    else:
        raise Exception(
            "Character config specifies {} edition, which does not exist".format(
                character.config["edition"]
            )
        )

    forms = character.getForms(request)

    character.build()

    exported = character.exportCharacter()

    if request.method == "GET":
        return Response(exported)


@api_view(["POST"])
def getCharacterWithToggles(request, characterId):
    character = get_object_or_404(Character, pk=characterId)
    config = json.loads(character.config)

    # TODO: Do this dynamically
    if config["edition"] == "5e":
        character = FifthEditionCharacter(character)
    elif config["edition"] == "Pathfinder":
        character = PathfinderCharacter(character)
    else:
        raise Exception(
            "Character config specifies {} edition, which does not exist".format(
                character.config["edition"]
            )
        )

    character.activeToggles = request.data

    character.build()

    exported = character.exportCharacter()

    return Response(exported)


@api_view(["GET"])
def getPlan(request, characterId):
    character = get_object_or_404(Character, pk=characterId)
    config = json.loads(character.config)

    # TODO: Do this dynamically
    if config["edition"] == "5e":
        character = FifthEditionCharacter()
    elif config["edition"] == "Pathfinder":
        character = PathfinderCharacter().fromCharacter(character)
    else:
        raise Exception(
            "Character config specifies {} edition, which does not exist".format(
                character.config["edition"]
            )
        )

    plan = Plan().getPlan(character)

    if request.method == "GET":
        return Response(plan)


# @api_view(["GET"])
# def getDBItem(request, type, item):
#     url = "./5eDatabase/{type}/{item}.html".format(type=type, item=item)

#     # Scrape and write features to file
#     file = open(url, "w")
#     contents = get5eClassFeatures(item)
#     ret = ""
#     for line in contents:
#         ret += line

#     file.write(ret)
#     file.close()

#     file = open(url)
#     contents = file.read()
#     file.close()
#     return Response(contents)


@api_view(["GET"])
def getCreationOptions(request):
    ret = {}
    ret["Race"] = list(races.allRaces().keys())

    return Response(json.dumps(ret))


def create(request):
    # character = config_list['ezekiel']
    # character = character.apply(Character())

    # #TODO: Do this dynamically
    # if character.config['edition'] == '5e':
    #     character = FifthEditionCharacter().fromCharacter(character)
    # elif character.config['edition'] == 'Pathfinder':
    #     character = PathfinderCharacter().fromCharacter(character)
    # else:
    #     raise Exception("Character config specifies {} edition, which does not exist".format(character.config['edition']))

    # character.save()

    # return HttpResponse("Created")
    return HttpResponse("Uncomment")
