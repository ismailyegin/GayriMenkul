from django.db import models


class Gkurum(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=120, null=True)
    kobilid = models.IntegerField(null=True, blank=True, default=2)

    def __str__(self):
        return '%s' % (self.name)
