"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

network.py:
This file makes a networkx graph of the stations (nodes) en the connections
between the stations (edges). This file also contains a method that gives all
the possible trajectories
"""

import networkx as nx
import matplotlib.pyplot as plt
import data
import get_data
import csv
import pandas as pd
import numpy as np

def generate_graph(data):
    """
    data    :   dataset

    generates a graph of the data

    return  :   graph
    """
    G = nx.Graph()

    for connectie, time in data.items():
        G.add_edge(connectie[0], connectie[1], weight=time)

    return G

def find_all_trajectories(data, max_time):
    """
    data        :   dataset
    max_time    :   max time that a trajectory can take

    creates a dict with all the possible trajectories as keys and the trajectory time
    as value

    return  :   dict
    """
    dict_trajectories = {}
    testl = []
    G = generate_graph(data)
    for departure_station in get_data.list_of_stations(data):
        print(departure_station)
        for arrival_station in get_data.list_of_stations(data):
            if departure_station != arrival_station:
                for trajectories in list(nx.all_simple_paths(G, departure_station, arrival_station, cutoff=18)):
                    teller = 0
                    time = 0
                    for i in trajectories:
                        if teller < len(trajectories)-1 and (i, trajectories[teller+1]) in data:
                            time += int(data[(i, trajectories[teller+1])])
                            teller += 1
                        elif teller < len(trajectories)-1 and (trajectories[teller+1], i) in data:
                            time += int(data[(trajectories[teller+1], i)])
                            teller += 1

                    if len(trajectories) == 18:
                        testl.append(time)

                    if time < (max_time + 1) and tuple(trajectories)[::-1] not in dict_trajectories:
                        dict_trajectories[tuple(trajectories)] = time

    m = min(testl)

    l = []
    teller = 0
    for i, j in dict_trajectories.items():
        teller += 1
        l.append([i, j])

    # np.savetxt("All_trajects_nationaal.csv", l, delimiter =", ", fmt ='% s')

    # df = pd.DataFrame(l)
    # df.to_csv('All_trajects_nationaal.csv')

    return dict_trajectories

if __name__ == "__main__":
    G = generate_graph(data.generate_dict()["ConnectiesHolland.csv"])
    print(find_all_trajectories(data.generate_dict()["ConnectiesHolland.csv"], 120))
    plt.figure(1)
    pos=nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()
