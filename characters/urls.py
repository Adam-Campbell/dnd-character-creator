from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharacterList.as_view(), name='character_list'),
    path('new/', views.create_character, name='create_character'),
    path('<int:id>/', views.character_detail, name='character_detail'),
    path('<int:id>/edit/', views.edit_character, name='edit_character'),
]