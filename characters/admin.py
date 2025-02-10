from django.contrib import admin
from .models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'race', 'character_class')
    search_fields = ('name', 'race', 'character_class')
