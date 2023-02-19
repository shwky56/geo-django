from rest_framework import generics
from django.views.generic import TemplateView
from doctermapp.api.serializers import HosptallSerializer
from doctermapp.models import (
    County,
    Doctore,
    Hosptall,
    Street,
    
)


class HomeView(TemplateView):
    template_name = 'index.html'


class HosptallListAPIView(generics.ListCreateAPIView):
    queryset = Hosptall.objects.all()
    serializer_class = HosptallSerializer
    