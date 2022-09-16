from .models import Group
from django import forms
from django.contrib.auth import get_user_model


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'members']
        widgets = {
            'members': forms.CheckboxSelectMultiple,
        }
