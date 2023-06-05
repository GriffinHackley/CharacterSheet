from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib import admin

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models.FifthEditionCharacter import FifthEditionCharacter
from .models.PathfinderCharacter import PathfinderCharacter
from .models.Characters import Character

import json
admin.site.register(Character)

def index(request):
    character_list = Character.objects.order_by("name")

    context = {
        'character_list': character_list,
    }

    return render(request, 'sheet/index.html', context)

@api_view(['GET'])
def getCharacter(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    config = json.loads(character.config)

    #TODO: Do this dynamically
    if config['edition'] == '5e':
        character = FifthEditionCharacter().fromCharacter(character)
    elif config['edition'] == 'Pathfinder':
        character = PathfinderCharacter().fromCharacter(character)
    else:
        raise Exception("Character config specifies {} edition, which does not exist".format(character.config['edition']))

    forms = character.getForms(request)

    character.build()
    
    exported = character.exportCharacter()

    if request.method == 'GET':
        character = get_object_or_404(Character, pk=character_id)
        return Response(exported) 

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    config = json.loads(character.config)

    #TODO: Do this dynamically
    if config['edition'] == '5e':
        character = FifthEditionCharacter().fromCharacter(character)
    elif config['edition'] == 'Pathfinder':
        character = PathfinderCharacter().fromCharacter(character)
    else:
        raise Exception("Character config specifies {} edition, which does not exist".format(character.config['edition']))

    forms = character.getForms(request)

    character.build()    

    return render(request, 'sheet/detail.html', {'character': character, 'skill_list': character.skillList, 'forms':forms })

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