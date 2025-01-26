from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.UUIDField()
    character_class = models.UUIDField()
    character_class_skill_choices = models.JSONField(default=list)
    character_class_cantrip_choices = models.JSONField(default=list, blank=True)
    character_class_spell_choices = models.JSONField(default=list, blank=True)
    ability_points = models.JSONField(default=list)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100)
    alignment = models.CharField(max_length=100)
    background = models.CharField(max_length=500)
    traits = models.JSONField(default=list, blank=True)
    ideals = models.JSONField(default=list, blank=True)
    bonds = models.JSONField(default=list, blank=True)
    flaws = models.JSONField(default=list, blank=True)
    height = models.CharField(max_length=100)
    build = models.CharField(max_length=100)
    skin_tone = models.CharField(max_length=100)
    hair_color = models.CharField(max_length=100)
    hair_style = models.CharField(max_length=100)
    hair_length = models.CharField(max_length=100)
    hair_type = models.CharField(max_length=100)
    facial_hair_style = models.CharField(max_length=100)
    facial_hair_length = models.CharField(max_length=100)
    eye_color = models.CharField(max_length=100)
    eye_shape = models.CharField(max_length=100)
    distinguishing_features = models.JSONField(default=list, blank=True)
    clothing_style = models.CharField(max_length=200)
    clothing_colors = models.JSONField(default=list, blank=True)
    clothing_accessories = models.JSONField(default=list, blank=True)
    liked_by = models.ManyToManyField(User, related_name='liked_characters')

    def __str__(self):
        return self.name

