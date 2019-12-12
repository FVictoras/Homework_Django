from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from companies.forms import CompaniesForm
from companies.models import Companies


class CompaniesIndex(ListView):
    model = Companies
    context_object_name = 'all_companies'
    template_name = 'companies/companies_index.html'


class CreateCompanyView(CreateView):
    model = Companies
    template_name = 'companies/company_form.html'
    form_class = CompaniesForm

    def get_success_url(self):
        return reverse('company:index')


class UpdateCompanyView(UpdateView):
    model = Companies
    template_name = 'companies/company_form.html'
    form_class = CompaniesForm

    def get_success_url(self):
        return reverse('company:update_company', args=[self.object.id])


class DeleteCompanyView(DeleteView):
    model = Companies
    template_name = 'companies/company_form.html'
    form_class = CompaniesForm

    def get_success_url(self):
        return reverse('company:index')
