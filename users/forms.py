from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


ACCOUNT_TYPES = [
        ('READER', 'Reader'),
        ('AUTHOR', 'Author'),
        ]


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    type = forms.ChoiceField(choices=ACCOUNT_TYPES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'type']


class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['account_type']
