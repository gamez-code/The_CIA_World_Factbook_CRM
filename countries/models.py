from django.db import models
from continents.models import Continent
# Create your models here.
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    active_manager = ActiveManager()
    objects = models.Manager()

    def __str__(self):
        return self.name
