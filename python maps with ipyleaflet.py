# In[1]

from IPython.display import IFrame
documentation = IFrame(src='https://ipyleaflet.readthedocs.io/en/latest', width=1000, height=600)
display(documentation)
# In[2]

# imports
import ipyleaflet
# from ipyleaflet import map

# create map
basic_map = ipyleaflet.Map(zoom=8)
# basic_map = Map(zoom4)

# display map
#basic_map
display(basic_map)
# In[3]
# Types Map
import ipyleaflet
import ipywidgets
from ipyleaflet import basemaps, Map

radio_button = ipywidgets.RadioButtons(options=['Positron', 'DarkMatter', 'WorldStreepMap', 'DeLorme',
                                                'WorldTopoMap', 'WorldImagery', 'NatGeoWorldMap', 'HikeBike',
                                                'HyddaFull', 'Night', 'ModisTerra', 'Mapnik', 'HOT', 'OpenTopoMap',
                                                'Toner', 'Watercolor'],
                                        value='Positron',
                                        description='map types:')
def toggle_maps(map):
    if map == 'Positron': m = Map(zoom=2, basemap=basemaps.CartoDB.Positron)
    if map == 'DarkMatter': m = Map(zoom=1, basemap=basemaps.CartoDB.DarkMatter)
    if map == 'WorldStreetMap': m = Map(center=(40.67, -73.94),zoom=4, basemap=basemaps.Esri.WorldStreetMap)
    if map == 'DeLorme': m = Map(center=(-6.200000, 106.816666),zoom=5, basemap=basemaps.Esri.DeLorme)
    if map == 'WorldTopoMap': m = Map(center=(-6.200000, 106.816666),zoom=6, basemap=basemaps.Esri.WorldTopoMap)
    if map == 'WorldImagery': m = Map(center=(-6.200000, 106.816666),zoom=7, basemap=basemaps.Esri.WorldImagery)
    if map == 'NatGeoWorldMap': m = Map(center=(-6.200000, 106.816666),zoom=8, basemap=basemaps.Esri.NatGeoWorldMap)
    if map == 'HikeBike': m = Map(center=(-6.200000, 106.816666),zoom=9, basemap=basemaps.HikeBike.HikeBike)
    if map == 'HyddaFull': m = Map(center=(-6.200000, 106.816666),zoom=5, basemap=basemaps.Hydda.Full)
    if map == 'Night': m = Map(center=(-6.200000, 106.816666),zoom=4, basemap=basemaps.NASAGIBS.ViirsEarthAtNight2012)
    if map == 'ModisTerra': m = Map(center=(-6.200000, 106.816666),zoom=9, basemap=basemaps.NASAGIBS.ModisTerraTrueColorCR)
    if map == 'Mapnik': m = Map(center=(-6.200000, 106.816666),zoom=8, basemap=basemaps.OpenStreetMap.Mapnik)
    if map == 'HOT': m = Map(center=(-6.200000, 106.816666),zoom=7, basemap=basemaps.OpenStreetMap.HOT)
    if map == 'OpenTopoMap': m = Map(center=(-6.200000, 106.816666),zoom=6, basemap=basemaps.OpenTopoMap)
    if map == 'Toner': m = Map(center=(-6.200000, 106.816666),zoom=5, basemap=basemaps.Stamen.Toner)
    if map == 'Watercolor': m = Map(center=(-6.200000, 106.816666),zoom=4, basemap=basemaps.Stamen.Watercolor)
    display(m)

ipywidgets.interact(toggle_maps, map=radio_button)
# In[4]
# Marker

from ipyleaflet import Map, Marker
import geocoder

# location address
location = geocoder.osm('DKI Jakarta')

# to view location details use location.json

# latitude and longitude of location
latlng = [location.lat, location.lng]

# create map
maps_jakarta = Map(center=latlng)

# marker
marker = Marker(location=latlng, title='DKI Jakarta')
maps_jakarta.add_layer(marker)

# display_map
maps_jakarta

# In[5]
# Marker

from ipyleaflet import Map, Marker
import geocoder

# location address
location1 = geocoder.osm('DKI Jakarta') 
location2 = geocoder.osm('Jakarta Pusat')
location3 = geocoder.osm('Jakarta Timur')
location4 = geocoder.osm('Jakarta Barat')
location5 = geocoder.osm('Jakarta Selatan')

# to view location details use location.json

# latitude and longitude of location
latlng1 = [location1.lat, location1.lng]
latlng2 = [location2.lat, location2.lng]
latlng3 = [location3.lat, location3.lng]
latlng4 = [location4.lat, location4.lng]
latlng5 = [location5.lat, location5.lng]

# create map
maps_jakarta = Map(center=latlng1)

# marker
marker1 = Marker(location=latlng1, title = 'DKI Jakarta')
marker2 = Marker(location=latlng2, title = 'Jakarta Pusat')
marker3 = Marker(location=latlng3, title = 'Jakarta Timur')
marker4 = Marker(location=latlng4, title = 'Jakarta Barat')
marker5 = Marker(location=latlng5, title = 'Jakarta Selatan')
maps_jakarta.add_layer(marker1)
maps_jakarta.add_layer(marker2)
maps_jakarta.add_layer(marker3)
maps_jakarta.add_layer(marker4)
maps_jakarta.add_layer(marker5)

# display_map
maps_jakarta

# In[6]

location1.json
# In[7]
location2.json

# In[8]
location3.json
# In[9]
location4.json
# In[10]
location5.json
# In[11]

# Marker Cluster

from ipyleaflet import Map, Marker, MarkerCluster
import geocoder

m = Map(center=(-6.1753942, 106.827183), zoom=5)

marker6 = Marker(location=(-6.18233995, 106.84287153600738))
marker7 = Marker(location=(-6.26289085, 106.88222894692834))
marker8 = Marker(location=(-6.16156235, 106.74389124027667))
marker9 = Marker(location=(-6.28381815, 106.80486349194814))

marker_cluster = MarkerCluster(markers=(marker6, marker7, marker8, marker9))

m.add_layer(marker_cluster);
# display_map
m

# In[12]
# Multiple Marker

from ipyleaflet import Map, Marker
# install vega_datasets first from python.org python package index
from vega_datasets import data

# airports dataframe using vega_datasets
airports = data.airports()
airports = airports[:25]

# create map
airports_map = Map(center=(-6.1753942, 106.827183), zoom=8)

# plot airport locations
for (index, row) in airports.iterrows():
    marker = Marker(location=[row.loc['latitude'], row.loc['longitude']],
                    title=row.loc['name'] + ' ' + row.loc['city'] + ' ' + row.loc['state'])
    airports_map.add_layer(marker)

# display map
airports_map

# In[14]
# Overlay GeoJSON Layers

import ipyleaflet
from ipyleaflet import Map, GeoJSON
import json

# use geojson.io to create custom geojson files
# convert shapefiles to geojson using QGIS (Default CRS of WGS 84)

# load geo_json data
with open('D:/cks/belajar/indonesia-geojson-master/jakarta.geojson') as f:
    geo_json_jakarta = json.load(f)

# create map
geo_json_jakarta_map = ipyleaflet.Map(center=(-6.1753942, 106.827183))

# create geo_json layer with style attributes
geo_json_jakarta_layer = GeoJSON(data=geo_json_jakarta,
                                 style = {'color':'blue',
                                 'opacity': 1.0,
                                 'weight': 1.9,
                                 'fill':'red',
                                 'fillOpacity': 0.5})

# add geo_json layer to map
geo_json_jakarta_map.add_layer(geo_json_jakarta_layer)

# display map
display(geo_json_jakarta_map)
# In[15]
# choropleth Map

import ipyleaflet
import json
import pandas as import pd
from branca.colormap import linear
import branca.colormap as cm
import numpy as np

# load geo_json
with open('D:/cks/belajar/indonesia-geojson-master/jakarta.geojson') as f:
    geo_json_data = json.load(f)

# load data associated with geo_json
pop_df = 

# In[16]
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBQ4MrOpZVoBaTYAesnQRb7px0iI60w9Lo')
now = datetime.now()
directions_result = gmaps.directions('-6.159843, 106.8534445','-6.1599934, 106.6872184', mode='driving', avoid='car', departure_time=now)

print(directions_result[0]['legs'][0]['distance']['text'])
print(directions_result[0]['legs'][0]['duration']['text'])

# In[17]

# gratis API 90 hari dari tgl 8/9/2020
import googlemaps 
  
# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyBQ4MrOpZVoBaTYAesnQRb7px0iI60w9Lo') 
  
# Requires cities name 
my_dist = gmaps.distance_matrix('Bogor', 'Jakarta Timur')['rows'][0]['elements'][0]
  
# Printing the result 
print(my_dist)

# In[18]

# gratis API 90 hari dari tgl 8/9/2020
import googlemaps 
  
# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyBQ4MrOpZVoBaTYAesnQRb7px0iI60w9Lo') 
  
# Requires cities name 
my_dist = gmaps.distance_matrix('Surabaya', 'Jakarta Pusat')['rows'][0]['elements'][0]
  
# Printing the result 
print(my_dist)