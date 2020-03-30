import folium
import pandas as pd

data = pd.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])

def popupColor(el):
    if el < 2000:
        return "green"
    else:
        return "red"

map = folium.Map(location = [38.58, -99.89], zoom_start = 6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el in zip(lat, lon, elevation):
    fg.add_child(folium.Marker(location = [lt, ln], popup = str(el) + " meters", icon=folium.Icon(color=popupColor(el))))
map.add_child(fg)

map.save("Map1.html")