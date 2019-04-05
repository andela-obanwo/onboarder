from django.db import models

from api.models.departments import Departments


class OnboardingItems(models.Model):

    PRESTART = 'prestart'
    POSTSTART = 'poststart'

    name = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(Departments)

    def __str__(self):
        return "{}: {}".format(self.name, self.type)