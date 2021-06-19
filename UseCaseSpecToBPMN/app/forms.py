from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import projectlist, scenariolist

class projectform(forms.ModelForm):
    class Meta:
        model=projectlist
        fields="__all__"
        widgets = {
            'usecasename' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'input your usecase name'}),
            'actor' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'input your actor'}),
            'precondition' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'what is your precondition?'}),
            'postcondition' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'what is your postcondition?'}),
        }

class scenarioform(ModelForm):
    class Meta:
        model=scenariolist
        fields="__all__"
        widgets ={
            'projectno' : forms.Select(attrs={'class':'form-control', 'placeholder':'input your usecase name'}),
            'scenarioid' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'input your Scenario ID'}),
            'scenariotype' : forms.Select(attrs={'class':'form-control'}),
            'postscenarioidyes' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'your post scenario id for yes'}),
            'postscenarioidno' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'your post scenario id for no'}),
            'scenario' : forms.TextInput(attrs={'class':'form-control','placeholder':'input your Scenario'})
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']