    import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[48.70, -121.70], zoom_start = 6, tiles= "Mapbox Bright" )

fgv = folium.FeatureGroup(name = "Volcanoes")
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location = [lt,ln], popup = str(el) + 'm',
    fill = True, fill_color = color_producer(el), radius = 6, color = 'grey', fill_opacity = 0.8))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = open("world.json", 'r', encoding = 'cp1252')read(),
style_function = lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 1000000
else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map99.html")
