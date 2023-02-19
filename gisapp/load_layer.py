# Auto-generated `LayerMapping` dictionary for Counties model

import os
from django.contrib.gis.utils import LayerMapping, LayerMapError
from gisapp.models import Counties, Provinces, Strite, Strite2

counties_mapping = {
    'adm0_en': 'ADM0_EN',
    'adm0_ar': 'ADM0_AR',
    'adm0_pcode': 'ADM0_PCODE',
    'adm0_ref': 'ADM0_REF',
    'adm0alt1en': 'ADM0ALT1EN',
    'adm0alt2en': 'ADM0ALT2EN',
    'adm0alt1ar': 'ADM0ALT1AR',
    'adm0alt2ar': 'ADM0ALT2AR',
    'date': 'date',
    'validon': 'validOn',
    'validto': 'validTo',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

provinces_mapping = {
    'adm1_en': 'ADM1_EN',
    'adm1_ar': 'ADM1_AR',
    'adm1_pcode': 'ADM1_PCODE',
    'adm1_ref': 'ADM1_REF',
    'adm1alt1en': 'ADM1ALT1EN',
    'adm1alt2en': 'ADM1ALT2EN',
    'adm1alt1ar': 'ADM1ALT1AR',
    'adm1alt2ar': 'ADM1ALT2AR',
    'adm0_en': 'ADM0_EN',
    'adm0_ar': 'ADM0_AR',
    'adm0_pcode': 'ADM0_PCODE',
    'date': 'date',
    'validon': 'validOn',
    'validto': 'validTo',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

strite_mapping = {
    'med_descri': 'MED_DESCRI',
    'rtt_descri': 'RTT_DESCRI',
    'f_code_des': 'F_CODE_DES',
    'iso': 'ISO',
    'isocountry': 'ISOCOUNTRY',
    'geom': 'MULTILINESTRING',
}

strite2_mapping = {
    'type': 'TYPE',
    'name': 'NAME',
    'oneway': 'ONEWAY',
    'lanes': 'LANES',
    'geom': 'MULTILINESTRING',
}
county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'egypt/data/strets2/egypt_highway.shp'))

def run(verbose=True):
    mapp = LayerMapping(Strite2, county_shp, strite2_mapping, transform=False, encoding='iso-8859-1')
    mapp.save(strict=True, verbose=verbose)

