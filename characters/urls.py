from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list, name='character_list'),
    path('new/', views.create_character, name='create_character'),
    path('<uuid:id>/', views.character_detail, name='character_detail'),
    path('<uuid:id>/edit/', views.edit_character, name='edit_character'),
]