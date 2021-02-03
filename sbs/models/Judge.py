from django.contrib.auth.models import User
from django.db import models

from sbs.models.Communication import Communication
from sbs.models.Level import Level
from sbs.models.Person import Person


class Judge(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    communication = models.OneToOneField(Communication, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    grades = models.ManyToManyField(Level, related_name='Judgegrades')
    visa = models.ManyToManyField(Level, related_name='Judgevisa')

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    class Meta:
        default_permissions = ()
