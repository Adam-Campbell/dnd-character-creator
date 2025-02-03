from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

def get_default_image_url():
    return static('images/profile-image-placeholder.webp')

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, default="")
    profile_image_url = models.URLField(default=get_default_image_url)

    def __str__(self):
        return f"{self.user.username}'s profile"