from django.db import models

from numeAplicatie.models import Location


class Companies(models.Model):
    name = models.CharField('Company Name', max_length=200)
    website = models.CharField('Website', max_length=200)
    location = models.ForeignKey(Location, on_delete=models.ForeignKey)

    def __str__(self):
        return '{}-{}'.format(str(self.name), str(self.website))

