from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


from doctermapp.models import (
    County,
    Doctore,
    Hosptall,
    Street,
    
)

class DoctoreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctore
        fields = '__all__'

class HosptallSerializer(GeoFeatureModelSerializer):
    
    doctores = DoctoreSerializer(read_only=True, many=True)
    
    class Meta:
        model = Hosptall
        geo_field = 'location'
        fields = ('name', 'doctores', 'street_name')
        