from django import forms
from django.forms import TextInput, Select

from companies.models import Companies


class CompaniesForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = ['name', 'website', 'location']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name of company', 'class': 'form-control'}),
            'website': TextInput(attrs={'placeholder': 'Website of company', 'class': 'form-control'}),
            'location': Select(attrs={'class': 'form-control'}),
        }
