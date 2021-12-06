import folium
import pandas


def color_producer(number):
    if number < 1000:
        x = "green"
    elif 1000 <= number < 3000:
        x = "orange"
    else:
        x = "red"
    return x


mp = folium.Map(location=[48, -120], zoom_start=8, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[6.641046485502927, 3.3578589472721916], popup="Light made me!",
                           icon=folium.Icon(color='green')))

df = pandas.read_csv("Volcanoes.txt", sep=",")

lat = list(df['LAT'])
lon = list(df['LON'])
elev = list(df['ELEV'])

fgv = folium.FeatureGroup(name="Volcanoes")


for i, j, L in zip(lat, lon, elev):
    fgv.add_child(
        folium.CircleMarker(location=(i, j), radius=6, popup=f"elevation {L}m", fill_color=color_producer(number=L),
                            color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', "r", encoding='utf-8-sig').read(),
                            style_function=lambda x: {
                                'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
mp.add_child(fgp)
mp.add_child(fgv)

mp.add_child(folium.LayerControl())
mp.save("Map1.html")
