from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email",
                "password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
