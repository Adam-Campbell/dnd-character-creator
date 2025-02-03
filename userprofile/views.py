from django.shortcuts import render
from django.contrib.auth.models import User
from characters.models import Character

# Create your views here.

def profile(request, user_id):
    # get the user and related user profile
    user = User.objects.select_related('userprofile').get(id=user_id)
    # grab the created characters for the user
    created_characters = Character.objects.filter(user=user)

    is_own_profile = (user == request.user)
    return render(request, 'userprofile/profile.html', {  'user': user, 'created_characters': created_characters, 'is_own_profile': is_own_profile })