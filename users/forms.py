from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms.widgets import DateInput

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name','last_name','date_of_birth','username', 'email','gender')
        labels = {
        'date_of_birth': ('D.O.B'),
        }
        widgets = {
        'date_of_birth': DateInput(attrs={'type': 'date'},format="%Y-%m-%d"),
        'gender': forms.RadioSelect()

        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','date_of_birth','username', 'email','gender')
        labels = {
        'date_of_birth': ('D.O.B'),
        }
        widgets = {
        'date_of_birth': DateInput(attrs={'type': 'date'})
        }
