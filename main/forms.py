from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets

from .models import Task


class TaskForm(ModelForm):
    """Form for task creating"""
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task\'s name'
            }),
            'task': widgets.Textarea(attrs={
                'class': 'form-control',
                'id': 'exampleInputPassword1',
                'placeholder': 'Describe your task here'
            })
        }

class UserRegisterForm(UserCreationForm):
    """Form for register account"""

    class Meta:
            model = User
            fields = ['username', 'password1', 'password2']
            help_texts = {
                'username': None,
                'password1': None,
            }