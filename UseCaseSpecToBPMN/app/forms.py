from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import projectlist, scenariolist

class projectform(ModelForm):
    class Meta:
        model=projectlist
        fields="__all__"

class scenarioform(ModelForm):
    class Meta:
        model=scenariolist
        fields="__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']