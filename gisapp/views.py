from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse  
from gisapp.models import Provinces, Incidences

class HomeView(TemplateView):
    template_name = 'Home.html'



def county_datasets(request):
	counties = serialize('geojson', Provinces.objects.all())
	return HttpResponse(counties,content_type='json')

def point_datasets(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points,content_type='json')
