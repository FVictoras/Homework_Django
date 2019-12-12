from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView

from numeAplicatie.forms import LocationForm
from numeAplicatie.models import Location


class HomeIndex(ListView):
    model = Location
    template_name = 'locations_index.html'
    context_object_name = 'all_locations'




class CreateLocation(CreateView):
    model = Location
    form_class = LocationForm
    # fields = ['country']
    template_name = 'location.html'

    def get_form_kwargs(self):
        kwargs = super(CreateLocation, self).get_form_kwargs()
        kwargs.update({'test': None})
        return kwargs

    def get_success_url(self):
        return reverse('app1:home')


class UpdateIndex(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'location.html'

    def get_queryset(self):
        return self.model.objects.filter(id=4)

    def get_form_kwargs(self):
        kwargs = super(UpdateIndex, self).get_form_kwargs()
        kwargs.update({'test': self.kwargs['pk']})
        return kwargs

    def get_success_url(self):
        return reverse('app1:home')

