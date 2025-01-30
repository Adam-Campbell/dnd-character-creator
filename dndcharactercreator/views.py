from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return redirect('characters:character_list')
    else:
        return redirect('about')

def about(request):
    return render(request, 'about.html')