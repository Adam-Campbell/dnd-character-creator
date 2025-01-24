from django.shortcuts import render

# Create your views here.
def character_list(request):
    return render(request, 'characters/character_list.html')

def create_character(request):
    return render(request, 'characters/create_character.html')

def character_detail(request, id):
    context = { 'id': id }
    return render(request, 'characters/character_detail.html', context)

def edit_character(request, id):
    context = { 'id': id }
    return render(request, 'characters/edit_character.html', context)