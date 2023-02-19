from django.urls import path

from gisapp.views import HomeView, county_datasets, point_datasets
from gisapp.api.views import ProvincesListAPIView,ProvincesDetailAPIView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('county_data/', county_datasets, name = 'county'),
    path('incidence_data/', point_datasets, name = 'incidences'),
    path("provinces/", ProvincesListAPIView.as_view(), name="pr"),
    path("provinces/<int:pk>/", ProvincesDetailAPIView.as_view(), name=""),
]

