from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models

class Incidences(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField(srid=4326)
    # objects = models.GeoManager()
    
    def __unicode__(self):
        return self.name


class Counties(models.Model):
    adm0_en = models.CharField(max_length=50, null=True)
    adm0_ar = models.CharField(max_length=50, null=True)
    adm0_pcode = models.CharField(max_length=50, null=True)
    adm0_ref = models.CharField(max_length=50, null=True)
    adm0alt1en = models.CharField(max_length=50, null=True)
    adm0alt2en = models.CharField(max_length=50, null=True)
    adm0alt1ar = models.CharField(max_length=50, null=True)
    adm0alt2ar = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    validon = models.DateField(null=True)
    validto = models.DateField(null=True)
    shape_leng = models.FloatField(null=True)
    shape_area = models.FloatField(null=True)
    geom = models.MultiPolygonField(srid=4326)
    
    def __unicode__(self):
        return  self.adm0_ar

class Provinces(models.Model):
    adm1_en = models.CharField(max_length=50, null=True)
    adm1_ar = models.CharField(max_length=50, null=True)
    adm1_pcode = models.CharField(max_length=50, null=True)
    adm1_ref = models.CharField(max_length=50, null=True)
    adm1alt1en = models.CharField(max_length=50, null=True)
    adm1alt2en = models.CharField(max_length=50, null=True)
    adm1alt1ar = models.CharField(max_length=50, null=True)
    adm1alt2ar = models.CharField(max_length=50, null=True)
    adm0_en = models.CharField(max_length=50, null=True)
    adm0_ar = models.CharField(max_length=50, null=True)
    adm0_pcode = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    validon = models.DateField(null=True)
    validto = models.DateField(null=True)
    shape_leng = models.FloatField(null=True)
    shape_area = models.FloatField(null=True)
    geom = models.MultiPolygonField(srid=4326)


class Strite(models.Model):
    med_descri = models.CharField(max_length=254, null=True)
    rtt_descri = models.CharField(max_length=254, null=True)
    f_code_des = models.CharField(max_length=10, null=True)
    iso = models.CharField(max_length=7, null=True)
    isocountry = models.CharField(max_length=54, null=True)
    geom = models.MultiLineStringField(srid=4326, null=True)

class Strite2(models.Model):
    type = models.CharField(max_length=22, null=True)
    name = models.CharField(max_length=113, null=True)
    oneway = models.CharField(max_length=17, null=True)
    lanes = models.BigIntegerField(null=True)
    geom = models.MultiLineStringField(srid=4326, null=True)

