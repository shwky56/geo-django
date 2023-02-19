from rest_framework.viewsets import ViewSet
from rest_framework import generics

from gisapp.models import Provinces
from gisapp.api.serializers import ProvincesSerializer

class ProvincesListAPIView(generics.ListAPIView):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer

class ProvincesDetailAPIView(generics.RetrieveAPIView):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer
