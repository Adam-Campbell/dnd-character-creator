from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from cloudinary.models import CloudinaryField

def get_default_image_url():
    return static('images/profile-image-placeholder.webp')

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, default="")
    image = CloudinaryField('image', default='profile-image-placeholder_lrxiao')

    def __str__(self):
        return f"{self.user.username}'s profile"