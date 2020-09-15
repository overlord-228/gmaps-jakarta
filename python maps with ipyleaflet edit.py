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

import folium
from folium import Map, Marker
import ipywidgets
import geocoder
import geopy.distance
import geopy.timezone
from IPython.core.display import display
from IPython.core.getipython import get_ipython

# location address
#location = geocoder.osm('DKI Jakarta')

# to view location details use location.json

# latitude and longitude of location
#latlng = [location.lat, location.lng]

# text widgets
route_start_widget = ipywidgets.Text(value='', placeholder='address', description='start:')
route_stop_widget = ipywidgets.Text(value='', placeholder='address', description='stop:')

# widget function
def get_distance(start_address, stop_address):
    
    # string addresses to location information
    start_location = geocoder.osm(start_address)
    stop_location = geocoder.osm(stop_address)
    
    # pull out latitude and longitude from location information
    start_latlng = [start_location.lat, start_location.lng]
    stop_latlng = [stop_location.lat, stop_location.lng]

       # calculate distance from start point to stop point using latitudes and longitudes
    distance = geopy.distance.distance(start_latlng, stop_latlng).miles
    print(f'distance: {distance:.2f} miles')

    # calculate duration from start point to stop point using latitudes and longitudes
    duration = geopy.Timezone.pytz_timezone(start_latlng, stop_latlng).minutes
    print(f'time: {time:.2f} minutes')
    
    # map
    distance_path = [(start_latlng), (stop_latlng)]
    map_distance = folium.Map(location=[-6.2293867,106.6894301], zoom_start=4)
    plugins.AntPath(distance_path).add_to(map_distance)
    display(map_distance)
    
# interaction between widgets and function    
ipywidgets.interact_manual(get_distance, start_address=route_start_widget, stop_address=route_stop_widget)

# create map
#maps_jakarta = Map(center=latlng)

# marker
# = Marker(location=latlng, title='DKI Jakarta')
#maps_jakarta.add_layer(marker)
  
# Requires API key 
#gmaps = googlemaps.Client(key='AIzaSyBQ4MrOpZVoBaTYAesnQRb7px0iI60w9Lo') 
  
# Requires cities name 
#my_dist = gmaps.distance_matrix('Bogor', 'Jakarta Timur')['rows'][0]['elements'][0]
  
# Printing the result 
#print(my_dist)

# In[18]

# gratis API 90 hari dari tgl 8/9/2020
import googlemaps 
  
# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyBQ4MrOpZVoBaTYAesnQRb7px0iI60w9Lo') 
  
# Requires cities name 
my_dist = gmaps.distance_matrix('Surabaya', 'Jakarta Pusat')['rows'][0]['elements'][0]
  
# Printing the result 
print(my_dist)

# In[18]

import geocoder
import ipyleaflet
from ipyleaflet import Map

# get location data for large cities (latitude and longitude)
jak_sel = geocoder.osm('Jakarta Selatan')
jak_bar = geocoder.osm('Jakarta Barat')
jak_tim = geocoder.osm('Jakarta Timur')
jak_ut = geocoder.osm('Jakarta Utara')

# create latitude, longitude, intensity for heat map
# intensity is population scaled down so heat dots are more readable
jaksel_latlng = [jak_sel.lat, jak_sel.lng, 1500000/1000]
jakbar_latlng = [jak_bar.lat, jak_bar.lng, 2500000/1000]
jaktim_latlng = [jak_tim.lat, jak_tim.lng, 4500000/1000]
jakut_latlng = [jak_ut.lat, jak_ut.lng, 5500000/1000]

# create list of cities with latitude, longitude, intensity
large_jakarta = [jakbar_latlng, jaksel_latlng, jaktim_latlng, jakut_latlng]

# create map
jakarta_heatmap = Map(center=(-6.1753942, 106.827183), zoom=4)

# create heatmap layer
heatmap_layer = ipyleaflet.Heatmap(locations=large_jakarta, radius=30, blur=20)

# add heatmap layer to map
jakarta_heatmap.add_layer(heatmap_layer)

# display map
jakarta_heatmap

# In[19]

from ipyleaflet import Map, FullScreenControl

# create map
full_screen_map = Map(zoom=1)

# create control
control = FullScreenControl()

# add control to map
full_screen_map.add_control(control)

# display map
full_screen_map

# In[20]

import ipyleaflet
from ipyleaflet import DrawControl

# create map
draw_control_map = ipyleaflet.Map(zoom=1)

# create control
draw_control = DrawControl()

# add control to map
draw_control_map.add_control(draw_control)

# add extra options to control
draw_control.circle = {
    "shapeOptions": {
        "fillColor": "blue",
        "color": 'blue',
        "fillOpacity": 0.5
    }
}

# display map
draw_control_map
# In[21]

import ipyleaflet
from ipyleaflet import MeasureControl

# create map
measure_control_map = ipyleaflet.Map(zoom=1)

# create control
measure = MeasureControl(position='topleft', active_color='red', primary_length_unit='miles')

# add control to map
measure_control_map.add_control(measure)

# measure line color
measure.completed_color='red'

# display map
measure_control_map

# In[22]

import ipyleaflet
from ipyleaflet import basemaps, basemap_to_tiles, SplitMapControl

# create map
split_map = ipyleaflet.Map(zoom=1)

# create right and left layers
right_layer = basemap_to_tiles(basemaps.Esri.WorldStreetMap)
left_layer = basemap_to_tiles(basemaps.NASAGIBS.ViirsEarthAtNight2012)

# create control
control = SplitMapControl(left_layer=left_layer, right_layer=right_layer)

# add control to map
split_map.add_control(control)

# display map
split_map
# In[23]

from ipyleaflet import Map, Marker
import geocoder
import ipywidgets

address_text_box = ipywidgets.Text(value='',
                                   placeholder='tulis disini',
                                   description='alamat',
                                   disabled=False)

def plot_locations(alamat):
    # location address
    location = geocoder.osm(alamat)

    # latitude and longitude of location
    latlng = [location.lat, location.lng]

    # create map
    plot_locations_map = Map(center=latlng, zoom=16)

    # marker
    marker = Marker(location=latlng, title=str(alamat))
    plot_locations_map.add_layer(marker)

    # display map
    display(plot_locations_map)

ipywidgets.interact_manual(plot_locations, alamat=address_text_box)

# In[24]

#from ipyleaflet import Map, Marker
import geocoder
import ipywidgets
import folium
from folium import Map, Marker

address_text_box = ipywidgets.Text(value='',
                                   placeholder='tulis disini',
                                   description='alamat:')

def get_latlng(alamat):
    # location address
    location = geocoder.osm(alamat)

    # latitude and longitude of location
    latlng = [location.lat, location.lng]

    # create map
    get_latlng_map = folium.Map(center=(-6.1753942, 106.827183), zoom=15)

    # marker
    folium.Marker(latlng, popup=str(alamat), tooltip='click').add_to(get_latlng_map)
    
    # display map
    display(get_latlng_map)

ipywidgets.interact_manual(get_latlng, alamat=address_text_box)
# In[25]

# cobacoba
import folium
from folium import Map, Marker
import geopy.distance

route_start_widget = ipywidgets.Text(value='', placeholder='alamat', description='start:')
route_stop_widget = ipywidgets.Text(value='', placeholder='alamat', description='stop:')

def get_distance(start_alamat, stop_alamat):
    start_location = geocoder.osm(start_alamat)
    stop_location = geocoder.osm(stop_alamat)

    start_latlng = [start_location.lat, start_location.lng]
    stop_latlng = [stop_location.lat, stop_location.lng]

    distance = geopy.distance.Distance(start_latlng, stop_latlng).miles
    timezome = geopy.timezone.Timezone(start_latlng, stop_latlng).minutes
    print(f'distance: {distance:.2f} miles')
    print(f'timezone: {timezone:.2f} minutes')

    distance_path = [(start_latlng), (stop_latlng)]
    timezome_path = [(start_latlng), (stop_latlng)]
    map_distance = folium.Map(location=[-6.1753942, 106.827183], zoom=15)
    plugins.AntPath(distance_path).add_to(map_distance)
    plugins.AntPath(timezone_path).add_to(map_distance)
    display(map_distance)

    def get_timezone(start_alamat, stop_alamat):
        start_location = geocoder.osm(start_alamat)
        stop_location = geocoder.osm(stop_alamat)

        start_latlng = [start_location.lat, start_location.lng]
        stop_latlng = [stop_location.lat, stop_location.lng]

        timezome = geopy.timezone.Timezone(start_latlng, stop_latlng).minutes
        print(f'timezone: {timezone:.2f} minutes')

        timezome_path = [(start_latlng), (stop_latlng)]
        map_distance = folium.Map(location=[-6.1753942, 106.827183], zoom=15)
        plugins.AntPath(timezone_path).add_to(map_distance)
        display(map_distance)

ipywidgets.interact_manual(get_distance, start_alamat=route_start_widget, stop_alamat=route_stop_widget)

# In[26]

import folium
from folium import Map, Marker

map_3 = folium.Map(location=(-6.1753942, 106.827183), tiles='Stamen Terrain',
                   zoom_start=13)
folium.LatLngPopup().add_to(map_3)
display(map_3)