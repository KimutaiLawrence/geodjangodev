from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Counties, Incidences  # Import Incidences model

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def county_datasets(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='application/json')

def incidence_datasets(request):
    incidences = serialize('geojson', Incidences.objects.all())  # Assuming you have an Incidences model
    return HttpResponse(incidences, content_type='application/json')
