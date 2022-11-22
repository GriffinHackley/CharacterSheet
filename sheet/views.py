from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Character, PathfinderCharacter, FifthEditionCharacter
from .configs import configs

config_list = configs.allConfigs()

def index(request):
    character_list = []
    for name, value in config_list.items():
        character_list.append(value.apply(Character()))
    
    print(character_list)

    context = {
        'character_list': character_list,
    }

    return render(request, 'sheet/index.html', context)

def detail(request, character_id):
    for name, config in config_list.items():
        if not config.id == character_id:
            continue

        character = config.apply(Character())

        #TODO: Do this dynamically
        if character.config['edition'] == '5e':
            character = FifthEditionCharacter().fromCharacter(character)
        elif character.config['edition'] == 'Pathfinder':
            character = PathfinderCharacter().fromCharacter(character)
        else:
            raise Exception("Character config specifies {} edition, which does not exist".format(character.config['edition']))

        forms = character.getForms(request)
    
        character.build()

        return render(request, 'sheet/detail.html', {'character': character, 'skill_list': character.skillList, 'forms':forms })
    
    raise Exception("Character with id {} was not found".format(character_id))

def create(request):
    # TODO: Implement this
    test = Character.create()
    test.save()
    return HttpResponse("Created")

def delete(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    character.delete()
    return HttpResponse("Deleted")