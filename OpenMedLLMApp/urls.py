"""Define URL patterns for our App"""

from django.urls import path

from . import  views

app_name = 'OpenMedLLMApp'
urlpatterns = [
    # Home Page
    path('', views.index, name = 'index'),
]