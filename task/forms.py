from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name_text', 'description_text']
        labels = {
            'name_text': 'Name of new task',
            'description_text': 'Description'
        }
        widgets = {
            'name_text': forms.Textarea(attrs={'cols': 40, 'rows': 1}),
            'description_text': forms.Textarea(attrs={'cols': 40, 'rows': 3})
        }