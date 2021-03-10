from django.db import models

from sbs.models.City import City
from sbs.models.Town import Town


class Gbolge(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, verbose_name='sehir', null=False, blank=False)
    town = models.ForeignKey(Town, on_delete=models.SET_NULL, verbose_name='ilce', null=True, blank=True)
