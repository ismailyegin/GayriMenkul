from django.db import models


class Punishment(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    startDate = models.DateTimeField()
    expireDate = models.DateTimeField()
    durationDay = models.IntegerField()
    #definition = models.ForeignKey(CategoryItem, on_delete=models.CASCADE)
    description = models.CharField(blank=True, null=True, max_length=1000)
    kobilid = models.IntegerField(null=True, blank=True, default=2)

    class Meta:
        default_permissions = ()
