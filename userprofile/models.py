from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, default="")
    image = CloudinaryField(
        'image',
        default='profile-image-placeholder_lrxiao'
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
