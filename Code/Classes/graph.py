"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

graph.py:
defines the Graph class as well as functions to manipulate it
"""
import csv
import os
#from turtle import circle
from .node import Node
import networkx as nx
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class Graph():
    def __init__(self, size):
        self.size = size # Holland/Nationaal
        self.stations_location = self.get_file_location(size, 'stations')
        self.connections_location = self.get_file_location(size, 'connections')
        self.nodes = self.load_stations()
        self.nx_graph = nx.Graph()
        self.load_connections()
        self.number_of_connections = self.number_of_connections()

    def get_file_location(self, size, type):
        """
        size    :   size of dataset: either 'Holland' or 'Nationaal'
        type    :   type of data, either 'stations' or 'connections'

        this function gives the file path for the proper .csv file
        """
        if type == 'stations':
            path_file = os.path.dirname(os.path.abspath(__file__))[0:-8] + '/../Datasets/Stations' + size + '.csv'
        else:
            path_file = os.path.dirname(os.path.abspath(__file__))[0:-8] + '/../Datasets/Connecties' + size + '.csv'
        return path_file

    def load_stations(self):
        """
        loads every station in a Node class
        """
        file = self.stations_location
        nodes = {}

        # open file with station information
        with open(file, "r") as f:
            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)

            for row in csv_reader:
                print(row)
                nodes[row[0]] = Node(row[0], row[1], row[2])
        return nodes

    def load_connections(self):
        """
        load all connections into Node classes, and into networkx graph
        """
        file = self.connections_location
        connections = {}

        # open file with connection information
        with open(file, "r") as f:
            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)

            # add all connections to all Node instances, and to networkx graph
            for row in csv_reader:
                self.nodes[row[0]].add_neighbour(row[1], float(row[2]))
                self.nodes[row[1]].add_neighbour(row[0], float(row[2]))

                self.nx_graph.add_edge(row[0], row[1], weight=row[2])

        # plt.rcParams["figure.figsize"] = [7.50, 3.50]
        # nx.draw(self.nx_graph, with_labels= True)
        # plt.show()
        # print(list(nx.all_simple_paths(self.nx_graph, 'Maastricht', 'Heerlen', cutoff=18)))

    def add_afsluitdijk(self):
        self.nodes['Den Helder'].add_neighbour('Leeuwarden', 30.0)
        self.nodes['Leeuwarden'].add_neighbour('Den Helder', 30.0)

        self.nx_graph.add_edge('Den Helder', 'Leeuwarden', weight=30.0)

    def remove_station(self, deleted_station_str):
        deleted_station = self.nodes[deleted_station_str]

        for station in self.nodes:
            if deleted_station_str in self.nodes[station].neighbours:
                self.nodes[station].remove_neighbour(deleted_station_str)
        self.nodes.pop(deleted_station_str)

    def number_of_connections(self):
        total_connections = 0

        for station in self.nodes:
            total_connections += len(self.dic_of_connections()[station])

        return total_connections/2

    def list_of_nodes(self):
        """
        returns list of the nodes (stations)
        """
        return [*self.nodes]

    def dic_of_connections(self):
        """
        returns dictionary of all connections
        """
        dict = {}

        for node in self.list_of_nodes():
            dict[node] = self.nodes[node].neighbours
        return dict

    def list_of_connections(self):
        """
        returns list of all connections
        """
        l = []
        for stations, n in self.dic_of_connections().items():
            for neighbors in n:
                if (neighbors, stations) not in l:
                    l.append((stations, neighbors))

        return l

    def find_all_trajectories(self, max_time):
        """
        max_time    :   max time that a trajectory can take

        creates a dict with all the possible trajectories as keys and the trajectory time
        as value

        return  :   dict
        """
        dict_trajectories = {}
        for departure_station in self.list_of_nodes():
            for arrival_station in self.list_of_nodes():
                if departure_station != arrival_station:
                    for trajectory in list(nx.all_simple_paths(self.nx_graph, departure_station, arrival_station, cutoff=18)):
                        total_time = 0
                        for i in range(len(trajectory)-1):
                            station1 = trajectory[i]
                            station2 = trajectory[i+1]

                            total_time += self.nodes[station1].neighbours[station2]

                        if total_time < (max_time + 1) and tuple(trajectory)[::-1] not in dict_trajectories:
                            dict_trajectories[tuple(trajectory)] = total_time
                else:
                    for station in self.dic_of_connections()[arrival_station]:
                        for trajectory in list(nx.all_simple_paths(self.nx_graph, arrival_station, station, cutoff=18)):
                            if len(trajectory) > 2:
                                trajectory.append(arrival_station)

                                total_time = 0

                                for i in range(len(trajectory)-1):
                                    station1 = trajectory[i]
                                    station2 = trajectory[i+1]

                                    total_time += self.nodes[station1].neighbours[station2]

                                if total_time < (max_time + 1) and tuple(trajectory)[::-1] not in dict_trajectories:
                                    dict_trajectories[tuple(trajectory)] = total_time

        # l = []
        # for i, j in dict_trajectories.items():
        #     l.append([i, j])

        # np.savetxt("All_trajects_nationaal.csv", l, delimiter =", ", fmt ='% s')

        # df = pd.DataFrame(l)
        # df.to_csv('All_trajects_nationaal.csv')
        return dict_trajectories


    # def find_all_trajectories(self, max_time):
    #     """
    #     max_time    :   max time that a trajectory can take

    #     creates a dict with all the possible trajectories as keys and the trajectory time
    #     as value

    #     return  :   dict
    #     """
    #     dict_trajectories = {}
    #     for departure_station in self.list_of_nodes():
    #         for arrival_station in self.list_of_nodes():
    #             if departure_station != arrival_station:
    #                 trajectory = list(nx.shortest_path(self.nx_graph, departure_station, arrival_station))
    #                 teller = 0
    #                 total_time = 0

    #                 for i in range(len(trajectory)-1):
    #                     station1 = trajectory[i]
    #                     station2 = trajectory[i+1]

    #                     total_time += self.nodes[station1].neighbours[station2]
    #                     teller += 1

    #                 if total_time < (max_time + 1) and tuple(trajectory)[::-1] not in dict_trajectories:
    #                     dict_trajectories[tuple(trajectory)] = total_time


    #     l = []
    #     teller = 0
    #     for i, j in dict_trajectories.items():
    #         teller += 1
    #         l.append([i, j])

    #     # np.savetxt("All_trajects_nationaal.csv", l, delimiter =", ", fmt ='% s')

    #     # df = pd.DataFrame(l)
    #     # df.to_csv('All_trajects_nationaal.csv')
    #     return dict_trajectories



