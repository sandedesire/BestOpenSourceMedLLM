"""Define URL patterns for our App"""

from django.urls import path

from . import  views

app_name = 'OpenMedLLMApp'
urlpatterns = [
    # Home Page
    path('', views.index, name = 'index'),

    # Page that shows all entries
    path('topics/', views.entries, name = 'entries'),

    # Page for Making a new Query

    path('new_query/', views.new_query, name = 'new_query'),
]