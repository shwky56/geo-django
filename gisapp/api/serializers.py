from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from gisapp.models import Provinces

class ProvincesSerializer(GeoFeatureModelSerializer):
    
    class Meta:
        model = Provinces
        geo_field = 'geom'
        fields = '__all__'