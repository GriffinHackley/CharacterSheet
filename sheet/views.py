import json

from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException

from .plan import Plan
from .races import races
from .models.Characters import Character
from .models.PathfinderCharacter import PathfinderCharacter
from .models.FifthEditionCharacter import FifthEditionCharacter

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
        raise APIException(
            "Character config specifies {} edition, which does not exist".format(
                character.config["edition"]
            )
        )

    try:
        character.build()

        exported = character.exportCharacter()
    except APIException as e:
        return HttpResponse(e, status=500)

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
        raise APIException(
            "Character config specifies {} edition, which does not exist".format(
                character.config["edition"]
            )
        )

    character.activeToggles = request.data

    try:
        character.build()
        exported = character.exportCharacter()
    except APIException as e:
        return HttpResponse(e, status=500)

    return Response(exported)


@api_view(["GET"])
def getPlan(request, characterId):
    character = get_object_or_404(Character, pk=characterId)
    config = json.loads(character.config)

    # TODO: Do this dynamically
    if config["edition"] == "5e":
        character = FifthEditionCharacter(character)
    elif config["edition"] == "Pathfinder":
        character = PathfinderCharacter().fromCharacter(character)
    else:
        raise APIException(
            "Character config specifies {} edition, which does not exist".format(
                character.config["edition"]
            )
        )

    plan = Plan().getPlan(character)

    if request.method == "GET":
        return Response(plan)


@api_view(["POST"])
def getGraph(request, characterId):
    character = get_object_or_404(Character, pk=characterId)
    # graph = cache.get(character.name + "_graph")
    requested_toggles = request.data

    # if graph and requested_toggles == graph["usedToggles"]:
    #     return Response(json.dumps(graph))

    # if not graph:
    graph = {}

    # cached_character = cache.get(character.name)
    cached_character = None
    if not cached_character:
        config = json.loads(character.config)
        if config["edition"] == "5e":
            character = FifthEditionCharacter(character)
        elif config["edition"] == "Pathfinder":
            character = PathfinderCharacter(character)
        else:
            raise APIException(
                "Character config specifies {} edition, which does not exist".format(
                    character.config["edition"]
                )
            )

        character.build()

    else:
        character = cached_character

    return Response(json.dumps(character.calculateGraph(requested_toggles)))


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
    #     raise APIException("Character config specifies {} edition, which does not exist".format(character.config['edition']))

    # character.save()

    # return HttpResponse("Created")
    return HttpResponse("Uncomment")
