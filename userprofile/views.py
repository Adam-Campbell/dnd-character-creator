from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from characters.models import Character
from .forms import BioForm
from characters.data_utils import get_static_data, get_item_by_id, get_image_url
from django.db.models import Q

# Create your views here.

def profile(request, user_id):
    # get the user and related user profile
    user = User.objects.select_related('userprofile').get(id=user_id)
    is_own_profile = (user == request.user)
    # grab static character data for enriching the characters
    static_character_data = get_static_data()

    # grab the created characters for the user
    if is_own_profile:
        created_characters = Character.objects.filter(user=user)
    else:
        created_characters = Character.objects.filter(user=user, is_public=True)
    for character in created_characters:
        character.image = get_image_url(character.image.public_id)
        character.class_data = get_item_by_id(static_character_data['classes'], str(character.character_class))
        character.race_data = get_item_by_id(static_character_data['races'], str(character.race))
    
    # grab the liked characters for the user
    if is_own_profile:
        liked_characters = user.liked_characters.filter(Q(is_public=True) | Q(user=user))
    else:
        liked_characters = user.liked_characters.filter(is_public=True)
    #liked_characters = user.liked_characters.all()
    for character in liked_characters:
        character.image = get_image_url(character.image.public_id)
        character.class_data = get_item_by_id(static_character_data['classes'], str(character.character_class))
        character.race_data = get_item_by_id(static_character_data['races'], str(character.race))

    
    return render(request, 'userprofile/profile.html', {  
        'user': user, 
        'created_characters': created_characters,
        'liked_characters': liked_characters,
        'is_own_profile': is_own_profile 
    })


@login_required
def edit_profile_bio(request, user_id):
    if request.method == 'POST':
        # grab the user and related user profile]
        user = User.objects.select_related('userprofile').get(id=user_id)
        # if the user is not the current user, return a 403
        if user != request.user:
            return HttpResponseForbidden("You are not allowed to edit this user's profile")
        form = BioForm(request.POST, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=user_id)

@login_required
def upload_profile_image(request, user_id):
    pass
