from django.urls import path
from . import views


urlpatterns = [
    path('<int:user_id>/', views.profile, name='profile'),
    path(
        '<int:user_id>/edit_bio/',
        views.edit_profile_bio,
        name='edit_profile_bio'
    ),
    path(
        '<int:user_id>/upload-image/',
        views.upload_profile_image,
        name='upload_profile_image'
    ),
]
