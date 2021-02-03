from django.contrib.auth.models import User
from django.db import models


class MenuDirectory(models.Model):
    name = models.CharField(max_length=120, null=True)
    url = models.CharField(max_length=120, null=True, blank=True)
    permission = models.ManyToManyField(User)
    is_parent = models.BooleanField(default=True)
    is_show = models.BooleanField(default=True)
    fa_icon = models.CharField(max_length=120, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    kobilid = models.IntegerField(null=True, blank=True, default=2)

    class Meta:
        default_permissions = ()
