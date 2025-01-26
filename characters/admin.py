from django.contrib import admin
from .models import Character

# Register your models here.

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'character_class', 'user')
    search_fields = ('name', 'race', 'character_class')
    filter_horizontal = ('liked_by',)
