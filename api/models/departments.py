from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name