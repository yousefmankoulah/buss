from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import user
from django.forms.boundfield import Textarea
from django.forms import ValidationError
from django.forms.fields import validators


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    college = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'college', 'email', 'password1', 'password2']
