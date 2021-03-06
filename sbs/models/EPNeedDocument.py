from django.db import models


class EPNeedDocument(models.Model):
    name = models.FileField(upload_to='Needdocument/', null=True, blank=True, verbose_name='NeedDocument')
    creationDate = models.DateTimeField(auto_now_add=True)
    operationDate = models.DateTimeField(auto_now=True)
    kobilid = models.IntegerField(null=True, blank=True, default=2)

    def __str__(self):
        return '%s ' % self.name
