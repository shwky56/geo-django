from django.db import models
from django.contrib.gis.db import models as gis_models

class Doctore(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=1000)

    def __str__(self) :
        return self.name

class Hosptall(models.Model):
    name = models.CharField(max_length=1000)
    doctores = models.ManyToManyField(Doctore)
    street_name = models.CharField(max_length=500)
    location = gis_models.PointField(null=False, srid=4326)
    
    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=1000)
    lode = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    geom = gis_models.LineStringField()
    
    def __str__(self):
        return self.name
    

class County(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=50, unique=True)
    geom = gis_models.PolygonField(srid=4326)
    
    def __str__(self):
        return self.name