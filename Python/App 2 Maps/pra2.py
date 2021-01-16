#--------------------Import Libraries
import folium
import pandas

#--------------------Reading .txt file and taking values
data = pandas.read_csv("Volcanoes.txt" )
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#--------------------Making function and giving values to color from elevation values
def color_producer(elevation):
    if elevation <1000:
        return 'Green'
    elif 1000<=elevation <3000:
        return 'Orange'
    else:
        return 'Red'

#--------------------Basic Code to start a Map
map = folium.Map(location = [38.58,-99.09], zoom_start=6, tiles="Mapbox Bright")

#--------------------Creating FeatureGroup
fgv = folium.FeatureGroup(name = "Volcanoes")
fgp = folium.FeatureGroup(name = "Population")

#--------------------Lat, Lon, values and Markers
for lt, lg, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, lg], radius =6, popup = str(el)+"m",
    fill_color = color_producer(el), fill = True, color = 'Grey', fill_opacity = 0.8))

#--------------------GeoJson File and its code
fgp.add_child(folium.GeoJson(data = open("world.json",'r', encoding = "cp1252").read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#--------------------Adding fg to map and saving it
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map2.html")
