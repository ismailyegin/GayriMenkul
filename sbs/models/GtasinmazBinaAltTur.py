from django.db import models

from sbs.models.GtasinmazBinaUstTur import GtasinmazUstTur


class GtasinmazAltTur(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    ust = models.ForeignKey(GtasinmazUstTur, on_delete=models.CASCADE, verbose_name='ust', )
    kobilid = models.IntegerField(null=True, blank=True, default=2)

    def __str__(self):
        return '%s' % (self.name)
