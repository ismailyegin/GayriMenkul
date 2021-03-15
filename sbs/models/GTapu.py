from django.db import models

from sbs.models.City import City
from sbs.models.Country import Country
from sbs.models.Town import Town


class GTapu(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)

    parcel = models.CharField(max_length=120, null=True, blank=True)
    island = models.CharField(max_length=120, null=True, blank=True)
    neighborhood = models.TextField(blank=True, null=True, verbose_name='Mahallle')
    town = models.ForeignKey(Town, on_delete=models.SET_NULL, verbose_name='İlce', db_column='town', blank=True,
                             null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, verbose_name='İl', db_column='city', blank=True,
                             null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name='Ülke', db_column='country',
                                blank=True, null=True)
    arsayuzolcumu = models.IntegerField(blank=True, null=True, )
    tahsisyuzolcumu = models.IntegerField(blank=True, null=True, )
    arsaEmsal = models.CharField(max_length=128, verbose_name='arsa_emsal', null=True, blank=True)

    kobilid = models.IntegerField(null=True, blank=True, default=2)
