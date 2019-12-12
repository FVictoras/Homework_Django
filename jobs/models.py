from django.db import models

# Create your models here.
from companies.models import Companies


class Jobs(models.Model):
    type = models.CharField('Job type', max_length=200)
    url = models.CharField('Job url', max_length=200)
    title = models.CharField('Job title', max_length=200)
    description = models.TextField('Job description', max_length=200)
    how_to_apply = models.TextField('Job applying', max_length=200)
    company = models.ForeignKey(Companies, on_delete=models.ForeignKey)
