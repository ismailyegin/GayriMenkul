from django.db import models


class EPRequirements(models.Model):
    amount = models.IntegerField(null=False, blank=False, default=0)
    definition = models.CharField(blank=False, null=False, max_length=255)
    creationDate = models.DateTimeField(auto_now_add=True)
    operationDate = models.DateTimeField(auto_now=True)
    kobilid = models.IntegerField(null=True, blank=True, default=2)
    class Meta:
        ordering = ['pk']
        default_permissions = ()
