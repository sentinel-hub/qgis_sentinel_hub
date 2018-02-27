#!/usr/bin/env python
# encoding: utf-8

# Base setup values
url_base = 'https://services.sentinel-hub.com/ogc/'

instance_id_location = "SentinelHub/instance_id"
download_folder_location = "SentinelHub/download_folder"

epsg = [
    'EPSG: 3857',
    'EPSG: 4326'
]

# Request parameters
parameters = {
    'name': 'sentinel2',
    'prettyName': 'Sentinel 2',
    'title': '',
    'showLogo': 'false',
    'layers': '',
    'maxcc': '20',
    'priority': 'mostRecent',
    'time': '',
    'crs': 'EPSG:3857'
}

parameters_wms = {  # The first 3 parameters are required for qgis layer
    'IgnoreGetFeatureInfoUrl': '1',
    'IgnoreGetMapUrl': '1',
    'contextualWMSLegend': '0',
    'service': 'WMS',
    'styles': '',
    'request': 'GetMap',
    'format': 'image/jpeg',
    'transparent': 'true',
    'version': '1.3.0',
}

parameters_wfs = {
    'service': 'WFS',
    'version': '2.0.0',
    'request': 'GetFeature',
    'typenames': 'S2.TILE',
    'maxfeatures': '100',
    'outputformat': 'application/json',
}

parameters_wcs = {
    'service': 'wcs',
    'request': 'GetCoverage',
    'format': 'image/png',
    'transparent': 'false',
    'version': '1.1.1',
    'resx': '10',
    'resy': '10'
}

# enum values of parameters
priority_list = ['mostRecent', 'leastRecent', 'leastCC']
atmfilter_list = ['NONE', 'DOS1', 'ATMCOR']
cloud_correction = ['NONE', 'REPLACE']
img_formats = ['image/png', 'image/jpeg',
               'image/tiff', 'image/tiff;depth=8', 'image/tiff;depth=16', 'image/tiff;depth=32f']
maxcc_range = [0, 100]
