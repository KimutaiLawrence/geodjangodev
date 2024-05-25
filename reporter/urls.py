from django.urls import path
from reporter.views import HomePageView, county_datasets, incidence_datasets  # Import the new view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('county_data/', county_datasets, name='county'),  # Note the trailing slash here
    path('incidence_data/', incidence_datasets, name='incidences'),  # Add this line
]
