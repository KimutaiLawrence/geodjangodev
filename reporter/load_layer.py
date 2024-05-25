import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties

counties_mapping = {
    'county_nam': 'COUNTY_NAM',
    'id': 'ID',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/counties.shp'))

def run(verbose=True):
    lm = LayerMapping(Counties, county_shp, counties_mapping, transform= False, encoding='iso-8859-1')
    lm.save(strict=True,verbose=verbose)