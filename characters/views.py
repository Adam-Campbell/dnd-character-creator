from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseNotFound
import json
from .models import Character
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.core.serializers import serialize
from .data_utils import normalise_character_data, validate_character_data


# Create your views here.
#def character_list(request):
#    return render(request, 'characters/character_list.html')

class CharacterList(generic.ListView):
    model = Character
    template_name = 'characters/character_list.html'
    context_object_name = 'characters'

    def get_queryset(self):
        return Character.objects.all()


@login_required
def create_character(request):
    if request.method == 'POST':
        print("POST request received")
        character_data = json.loads(request.body)
        new_character = Character.objects.create(
            user=request.user,
            race=character_data['race'],
            character_class=character_data['character_class'],
            character_class_skill_choices=character_data['character_class_skill_choices'],
            character_class_cantrip_choices=character_data['character_class_cantrip_choices'],
            character_class_spell_choices=character_data['character_class_spell_choices'],
            ability_points=character_data['ability_points'],
            name=character_data['name'],
            age=character_data['age'],
            gender=character_data['gender'],
            alignment=character_data['alignment'],
            background=character_data['background'],
            traits=character_data['traits'],
            ideals=character_data['ideals'],
            bonds=character_data['bonds'],
            flaws=character_data['flaws'],
            height=character_data['height'],
            build=character_data['build'],
            skin_tone=character_data['skin_tone'],
            hair_color=character_data['hair_color'],
            hair_style=character_data['hair_style'],
            hair_length=character_data['hair_length'],
            hair_type=character_data['hair_type'],
            facial_hair_style=character_data['facial_hair_style'],
            facial_hair_length=character_data['facial_hair_length'],
            eye_color=character_data['eye_color'],
            eye_shape=character_data['eye_shape'],
            distinguishing_features=character_data['distinguishing_features'],
            clothing_style=character_data['clothing_style'],
            clothing_colors=character_data['clothing_colors'],
            clothing_accessories=character_data['clothing_accessories']
        )
        new_character.save()
        print("Character created")
        return JsonResponse({ 'message': 'POST request handled' })
    # End of POST request handling
    return render(request, 'characters/create_character.html')




def character_detail(request, id):
    context = { 'id': id }
    return render(request, 'characters/character_detail.html', context)



@login_required
def edit_character(request, id):
    context = { 'id': id }
    if request.method == 'POST':
        character_data = json.loads(request.body)
        character = Character.objects.get(id=character_data['id'])
        #print(character)
        for (key, value) in character_data.items():
            if key == 'id':
                continue
            if key == 'user':
                continue
            if hasattr(character, key):
                setattr(character, key, value)
        character.save()
        return JsonResponse({ 'message': 'POST request handled' })
    # End of POST request handling
    try:
        character = Character.objects.get(id=id)
    # If the character does not exist, return a 404 error
    except Character.DoesNotExist:
        return HttpResponseNotFound("Character does not exist")
    # If the character does not belong to the user, return a 403 error
    if character.user != request.user:
        return HttpResponseForbidden("You do not have permission to edit this character")
    # If the character exists and belongs to the user, render the edit_character.html template
    context['character_data'] = character.to_json()
    return render(request, 'characters/edit_character.html', context)