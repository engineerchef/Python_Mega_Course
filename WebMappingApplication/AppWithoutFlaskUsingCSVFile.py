import folium
import pandas

df = pandas.read_csv("Files/Volcanoes.txt")
map = folium.Map(
    location=[
        df["LAT"].mean(), df["LON"].mean()
    ],
    zoom_start=5,
    tiles="Stamen Terrain"
    # tiles="Mapbox bright"
)


def color_is(elev):
    # =========================================================================================================

    # if elev < 1000:
    #     return "green"
    # elif 3000 > elev >= 1000:
    #     return "orange"
    # elif elev >= 3000:
    #     return "red"

    # =========================================================================================================

    # if elev in range(0, 1000):
    #     color = "green"
    # elif elev in range(1000, 3000):
    #     color = "orange"
    # else:
    #     color = "red"
    # return color

    # =========================================================================================================

    minimum = int(min(df["ELEV"]))
    step = int((max(df["ELEV"]) - min(df["ELEV"])) / 3)

    if elev in range(minimum, minimum + step):
        color = "green"
    elif elev in range(minimum, minimum + step * 2):
        color = "orange"
    else:
        color = "red"
    return color


fg = folium.FeatureGroup(name="Volcano Locations")

for lat, lon, name, elev in zip(df["LAT"], df["LON"], df["NAME"], df["ELEV"]):
    fg.add_child(folium.Marker(
        [lat, lon],
        popup=name,
        icon=folium.Icon(
            icon='info-sign',
            color=color_is(elev))
    ))

    # folium.Marker(
    #     [lat, lon],
    #     popup=(name, elev),
    #     icon=folium.Icon(
    #         icon='info-sign',
    #         color="green" if elev in range(0,1000) else "orange" if elev in range(1000,3000) else "red")).add_to(
    #     map
    # )

# =========================================================================================================
# That code below doesn't work properly
# dataFolder = 'Files'
# # dataFile = f'{dataFolder}/world.json'
# dataFile = open(dataFolder + "/world.json")
#
# # map.add_child(folium.GeoJson(data=dataFile, name="World Population"))
# folium.GeoJson(dataFile, name="World Population").add_to(map)

# map.add_child(folium.LayerControl())
# folium.LayerControl().add_to(map)

# =========================================================================================================

map.add_child(fg)

# map.add_child(folium.GeoJson(data=open('Files/world.json').read(),name='World Population'))
map.add_child(folium.LayerControl())
map.save(outfile='AppWithoutFlaskUsingCSVFile.html')
