from django.urls import path
from reporter.views import HomePageView, county_datasets

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('county_data/', county_datasets, name='county'),  # Note the trailing slash here
    path('incidence_data', HomePageView.as_view(), name='home'),
]
