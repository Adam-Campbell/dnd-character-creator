from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.CharacterList.as_view(), name='character_list'),
    path('new/', views.create_character, name='create_character'),
    path('<int:id>/', views.character_detail, name='character_detail'),
    path('<int:id>/edit/', views.edit_character, name='edit_character'),
    path('<int:character_id>/toggle_like/', views.toggle_like, name='toggle_like'),
    path('<int:character_id>/delete/', views.delete_character, name='delete_character'),
    path('<int:character_id>/toggle_privacy/', views.toggle_privacy, name='toggle_privacy'),
    path('<int:character_id>/clone/', views.clone_character, name='clone_character'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('generate-image/', views.generate_image, name='generate_image'),
]