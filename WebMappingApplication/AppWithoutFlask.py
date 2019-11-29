import folium
import pandas

# print(dir(folium))
map = folium.Map(location=[45.372, -121.697], zoom_start=12, tiles="Stamen Terrain")
folium.Marker([45.372, -121.697], popup="Mt. Hood Meadows",icon=folium.Icon(icon='info-sign', color='red')).add_to(map)

map.save(outfile='AppWithoutFlask.html')