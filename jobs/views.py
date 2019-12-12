from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from jobs.forms import JobsForm
from jobs.models import Jobs


class JobsIndex(ListView):
    model = Jobs
    context_object_name = 'all_jobs'
    template_name = 'jobs/jobs_index.html'


class CreateJobsView(CreateView):
    model = Jobs
    template_name = 'jobs/jobs_form.html'
    form_class = JobsForm

    def get_success_url(self):
        return reverse('jobs:index')


class UpdateJobsView(UpdateView):
    model = Jobs
    template_name = 'jobs/jobs_form.html'
    form_class = JobsForm

    def get_success_url(self):
        return reverse('jobs:update_job', args=[self.object.id])


class DeleteJobsView(DeleteView):
    model = Jobs
    template_name = 'jobs/jobs_form.html'
    form_class = JobsForm

    def get_success_url(self):
        return reverse('jobs:index')
