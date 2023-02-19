from django.contrib import admin

from gisapp.models import Incidences, Counties, Provinces, Strite, Strite2

from leaflet.admin import LeafletGeoAdmin

class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')

class CountiesAdmin(LeafletGeoAdmin):
    pass
    # list_display = ('adm0_en', 'adm0_ar')
class ProvincesAdmin(LeafletGeoAdmin):
    list_display = ('adm1_en', 'id', 'adm0_en',)

class StriteAdmin(LeafletGeoAdmin):
    pass
admin.site.register(Strite2, StriteAdmin)
admin.site.register(Strite, StriteAdmin)
admin.site.register(Provinces, ProvincesAdmin)
admin.site.register(Counties, CountiesAdmin)
admin.site.register(Incidences, IncidencesAdmin)
