from .models import Task
from django.forms import ModelForm, widgets

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ticket\'s name'
            }),
            'task': widgets.Textarea(attrs={
                'class': 'form-control',
                'id': 'exampleInputPassword1',
                'placeholder': 'Describe your problem'
            })
        }