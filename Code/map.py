"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

map.py:
this file generates a map with al the stations
"""
import folium
import data
import webbrowser

data = data.generate_dict()
stations = data['StationsHolland.csv']
connections = data['ConnectiesNationaal.csv']

map = folium.Map(location=[52.388, 4.638], zoom_start=8, tiles='Cartodb dark_matter')

for station in stations:
    stations[station] = (float(stations[station][0]), float(stations[station][1]))
    folium.CircleMarker(location=stations[station], radius=5, tooltip=station, color='#00C4B3', fill_color='#00C4B3', fill=True).add_to(map)

for connection in connections:
    points = [tuple(stations[connection[0]]), tuple(stations[connection[1]])]
    folium.PolyLine(locations=points, color='#00C4B3', weight=2.5, tooltip=connections[connection]).add_to(map)

def add_trajectory(list, color):
    """
    list    :   list of stations on trajectory
    color   :   color of trajectory

    this function adds a trajectory with color
    """

    for i in range(len(list) - 1):

        if (list[i], list[i+1]) in connections:
            connection = (list[i], list[i+1])
        else:
            connection = (list[i+1], list[i])

        points = stations[list[i]], stations[list[i+1]]
        folium.PolyLine(locations=points, color=color, weight=2.5, tooltip=connections[connection]).add_to(map)

add_trajectory(['Den Helder', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal'], '#F53044')

if __name__ == "__main__":
    map.save('Maps/HollandMap.html')
    webbrowser.open_new_tab('Maps/HollandMap.html')