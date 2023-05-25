from django.urls import path
from .views import IMDBView, filter

urlpatterns = [
    path('', IMDBView.as_view(), name='allrecords'),
    path('movies/', filter, name='filter'),
]