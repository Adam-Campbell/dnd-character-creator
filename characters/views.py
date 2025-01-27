from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseNotFound
import json
from .models import Character
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.core.serializers.json import DjangoJSONEncoder

    


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
        #print(request.user.is_authenticated)
        character_data = json.loads(request.body)
        #print(character_data)
        new_character = Character.objects.create(
            user=request.user,
            race=character_data['race'],
            character_class=character_data['class'],
            character_class_skill_choices=character_data['classSkillChoices'],
            character_class_cantrip_choices=character_data['classCantripChoices'],
            character_class_spell_choices=character_data['classSpellChoices'],
            ability_points=character_data['abilityPoints'],
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
            skin_tone=character_data['skinTone'],
            hair_color=character_data['hairColor'],
            hair_style=character_data['hairStyle'],
            hair_length=character_data['hairLength'],
            hair_type=character_data['hairType'],
            facial_hair_style=character_data['facialHairStyle'],
            facial_hair_length=character_data['facialHairLength'],
            eye_color=character_data['eyeColor'],
            eye_shape=character_data['eyeShape'],
            distinguishing_features=character_data['distinguishingFeatures'],
            clothing_style=character_data['clothingStyle'],
            clothing_colors=character_data['clothingColors'],
            clothing_accessories=character_data['clothingAccessories']
        )
        new_character.save()
        print("Character created")
        return JsonResponse({ 'message': 'POST request handled' })
    return render(request, 'characters/create_character.html')




def character_detail(request, id):
    context = { 'id': id }
    return render(request, 'characters/character_detail.html', context)



@login_required
def edit_character(request, id):
    context = { 'id': id }
    try:
        character = Character.objects.get(id=id)
    # If the character does not exist, return a 404 error
    except Character.DoesNotExist:
        return HttpResponseNotFound("Character does not exist")
    # If the character does not belong to the user, return a 403 error
    if character.user != request.user:
        return HttpResponseForbidden("You do not have permission to edit this character")
    # If the character exists and belongs to the user, render the edit_character.html template
    context['character_data'] = json.dumps({
        'name': character.name,
        'race': str(character.race),
        'class': str(character.character_class)
    })
    return render(request, 'characters/edit_character.html', context)