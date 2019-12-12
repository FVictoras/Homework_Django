from django.db import models

# Create your models here.

class Location(models.Model):
    # cityChoices = (('Bucuresti', 'Bucuresti'), ('Craiova', 'Craiova'))
    country = models.CharField('Country', max_length=100, blank=True, null=True)
    city = models.CharField('City', max_length=100, blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(str(self.country), str(self.city))

