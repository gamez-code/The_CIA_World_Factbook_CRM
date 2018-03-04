from django.db import models
from continents.models import Continent
# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
