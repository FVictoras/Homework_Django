from django import forms
from django.forms import TextInput, Select

from jobs.models import Jobs


class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['type', 'url', 'title', 'description', 'how_to_apply', 'company']

        widgets = {
            'type': TextInput(attrs={'placeholder': 'Type of job', 'class': 'form-control'}),
            'url': TextInput(attrs={'placeholder': 'URL', 'class': 'form-control'}),
            'title': TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Description', 'class': 'form-control'}),
            'how_to_apply': TextInput(attrs={'placeholder': 'How to apply', 'class': 'form-control'}),
            'company': Select(attrs={'class': 'form-control'})
        }
