from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from doctermapp.models import Doctore, Hosptall, County, Street

@admin.register(Doctore)
class DoctoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Hosptall)
class HosptallAdmin(gis_admin.OSMGeoAdmin):
    pass 

@admin.register(County)
class CountyAdmin(gis_admin.OSMGeoAdmin):
    pass 

@admin.register(Street)
class StreetAdmin(gis_admin.OSMGeoAdmin):
    pass 