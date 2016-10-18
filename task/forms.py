from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name_text', 'description_text', 'date_to_finish']
        labels = {
            'name_text': 'Name of new task',
            'description_text': 'Description',
            'date_to_finish': 'When i want to finish'
        }
        widgets = {
            'name_text': forms.Textarea(attrs={'cols': 40, 'rows': 1}),
            'description_text': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'date_to_finish': forms.DateInput(attrs={'class': 'datepicker'})
        }