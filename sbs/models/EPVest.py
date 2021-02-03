from django.db import models



class EPVest(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    operationDate = models.DateTimeField(auto_now=True)
    vestDate = models.DateField(blank=False, null=False)
    vest = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    kobilid = models.IntegerField(null=True, blank=True, default=2)



    class Meta:
        ordering = ['pk']
        default_permissions = ()