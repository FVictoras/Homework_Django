from django import forms
from django.forms import TextInput, Select

from numeAplicatie.models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['country', 'city']

        widgets = {
            'city': TextInput(attrs={'placeholder': 'City', 'class': 'field'}),
            'country': TextInput(attrs={'placeholder': 'Country', 'class': 'field'}),
        }

    def __init__(self, test, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.test = test

    def clean(self):
        cleaned_data = self.cleaned_data
        city_val = self.cleaned_data['city']
        country_val = self.cleaned_data['country']
        if self.test:
            all_locations = Location.objects.all().exclude(id=self.test)
        else:
            all_locations = Location.objects.all()
        for location in all_locations:
            if city_val == location.city and country_val == location.country:
                self._errors['city'] = 'Duplicate entry'
        return cleaned_data