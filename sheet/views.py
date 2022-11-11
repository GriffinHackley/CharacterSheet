from django.shortcuts import get_object_or_404, render

from .models import Character, PathfinderCharacter, FifthEditionCharacter
from .configs import neil, myriil


def index(request):
    character_list = Character.objects.order_by('name')

    context = {
        'character_list': character_list,
    }

    return render(request, 'sheet/index.html', context)

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    character = neil.apply(character)
    # character = myriil.apply(character)

    if character.config['edition'] == '5e':
        character = FifthEditionCharacter().fromCharacter(character)
    elif character.config['edition'] == 'Pathfinder':
        character = PathfinderCharacter().fromCharacter(character)

    if request.method == 'GET':
        forms = character.getForms(request)
    
    character.build()
    character.fullChar.save()

    return render(request, 'sheet/detail.html', {'character': character, 'skill_list': character.skillList, 'forms':forms })

def create(request):
    # TODO: Implement this
    # test = Character.create("5e", '8,17,14,10,16,8', "Myriil", "Ranger", 4, "Shadar-Kai", 'Spy', "Griffin", "Neutral Good", [], 0, {}, {}, {})
    # test.save()
    return HttpResponse("Created")

def delete(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    character.delete()
    return HttpResponse("Deleted")