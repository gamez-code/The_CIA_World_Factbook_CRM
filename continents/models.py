from django.db import models
# Create your models here.

class Continent(models.Model):
    name = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    color = models.CharField(max_length=8)
    code = models.CharField(max_length=3)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
