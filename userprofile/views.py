import cloudinary.uploader
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.db.models import Q
from characters.models import Character
from .forms import BioForm
from characters.data_utils import (
    get_static_data,
    get_item_by_id,
    get_image_url
)


def profile(request, user_id):
    """
    Renders the users profile page, showing their basic profile information,
    the characters they have created and the characters they have liked.
    """
    # get the user and related user profile
    user = User.objects.select_related('userprofile').get(id=user_id)
    user.userprofile.image = get_image_url(
        user.userprofile.image.public_id,
        width=250,
        height=250
    )
    is_own_profile = (user == request.user)
    # grab static character data for enriching the characters
    static_character_data = get_static_data()

    # grab the created characters for the user
    if is_own_profile:
        created_characters = Character.objects.filter(user=user)
    else:
        created_characters = Character.objects.filter(
            user=user,
            is_public=True
        )
    for character in created_characters:
        character.user.userprofile.image = get_image_url(
            character.user.userprofile.image.public_id,
            width=60,
            height=60
        )
        character.image = get_image_url(character.image.public_id)
        character.class_data = get_item_by_id(
            static_character_data['classes'],
            str(character.character_class)
        )
        character.race_data = get_item_by_id(
            static_character_data['races'],
            str(character.race)
        )

    # grab the liked characters for the user
    if is_own_profile:
        liked_characters = user.liked_characters.filter(
            Q(is_public=True) | Q(user=user)
        )
    else:
        liked_characters = user.liked_characters.filter(is_public=True)

    for character in liked_characters:
        character.user.userprofile.image = get_image_url(
            character.user.userprofile.image.public_id,
            width=60,
            height=60
        )
        character.image = get_image_url(character.image.public_id)
        character.class_data = get_item_by_id(
            static_character_data['classes'],
            str(character.character_class)
        )
        character.race_data = get_item_by_id(
            static_character_data['races'],
            str(character.race)
        )

    return render(request, 'userprofile/profile.html', {
        'user': user,
        'created_characters': created_characters,
        'liked_characters': liked_characters,
        'is_own_profile': is_own_profile
    })


@login_required
@require_http_methods(['POST'])
def edit_profile_bio(request, user_id):
    """
    Edit the user's bio information. This view is only accessible via POST.
    """
    # grab the user and related user profile]
    user = User.objects.select_related('userprofile').get(id=user_id)
    # if the user is not the current user, return a 403
    if user != request.user:
        return HttpResponseForbidden(
            "You are not allowed to edit this user's profile"
        )
    form = BioForm(request.POST, instance=user.userprofile)
    if form.is_valid():
        form.save()
        return redirect('profile', user_id=user_id)


@login_required
@require_http_methods(['POST'])
def upload_profile_image(request, user_id):
    """
    Upload a new profile image for the user. This view is only accessible via
    POST.
    """
    # grab the user and related user profile
    user = User.objects.select_related('userprofile').get(id=user_id)
    # if the user is not the current user, return a 403
    if user != request.user:
        return HttpResponseForbidden(
            "You are not allowed to edit this user's profile"
        )
    # grab the image from the request
    image = request.FILES['image']
    # upload the image to cloudinary
    upload_result = cloudinary.uploader.upload(image)
    # update the user profile image
    user.userprofile.image = upload_result['public_id']
    user.userprofile.save()
    return JsonResponse(
        {'message': 'Image uploaded successfully'},
        status=200
    )
