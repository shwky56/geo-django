
from django.urls import path

from doctermapp.api.view import HosptallListAPIView, HomeView

urlpatterns = [
    path("home/", HomeView.as_view(), name="ll"),
    path('', HosptallListAPIView.as_view(), name='hosptall')
]
