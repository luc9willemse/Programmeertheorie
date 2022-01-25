"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

map.py:
defines the Map class as well as functions to manipulate it
"""
import folium
import webbrowser
import seaborn as sns

class Map():
    def __init__(self, stations, connections, type):
        self.type = type
        self.stations = stations
        self.connections = connections
        self.colors = sns.color_palette("bright", 12).as_hex()
        self.create_map()

    def create_map(self):
        """
        creates a map object
        """
        # create map instance
        self.map = folium.Map(location=[52.388, 4.638], zoom_start=8, tiles='Cartodb dark_matter')
        print(self.colors)
        # add all stations as markers
        for station in self.stations:
            folium.CircleMarker(location=self.stations[station].location, radius=5, tooltip=station, color='#00C4B3', fill_color='#00C4B3', fill=True).add_to(self.map)

        # add connections between stations
        for station in self.connections:
            neighbours = self.connections[station]
            for neighbour in neighbours:
                points = [self.stations[station].location, self.stations[neighbour].location]
                folium.PolyLine(locations=points, color='#00C4B3', weight=2.5, tooltip=neighbours[neighbour]).add_to(self.map)

    def add_trajectory(self, stations, color):
        """
        stations    :   list of stations on trajectory
        color       :   color of trajectory

        adds a trajectory with color
        """

        group_name = stations[0] + ' - ' + stations[-1]
        feature_group = folium.FeatureGroup(group_name)

        for i in range(len(stations) - 1):
            station1 = self.stations[stations[i]]
            station2 = self.stations[stations[i+1]]
            value = self.connections[station1.name][station2.name]

            points = station1.location, station2.location
            folium.PolyLine(locations=points, color=color, weight=2.5, tooltip=value).add_to(feature_group)

        feature_group.add_to(self.map)

    def add_solution(self, list):
        """
        list    :   list of trajectories

        adds a solution consisting of trajectories
        """
        trajectories = list
        for trajectory in trajectories:
            color = self.colors[trajectories.index(trajectory)]
            self.add_trajectory(trajectory, color)

    def save_map(self):
        """
        saves the map in .html file and opens in browser
        """
        folium.LayerControl().add_to(self.map)
        self.map.save('Output/Maps/' + self.type + 'Map.html')
        webbrowser.open_new_tab('Output/Maps/' + self.type + 'Map.html')
