from django import forms
from .models import UserProfile


class BioForm(forms.ModelForm):
    """
    A form for updating a user's bio.
    """
    class Meta:
        model = UserProfile
        fields = ['bio']
