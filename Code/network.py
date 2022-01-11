"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

network.py:
this file makes a networkx graph of the stations (nodes) en the connections
between the stations (edges). this file also contains a method that gives all
the possible trajects
"""

import networkx as nx
import matplotlib.pyplot as plt
import data
import get_data

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

def find_all_trajects(data, max_time):
    """
    data        :   dataset
    max_time    :   max time that a traject can take

    creates a dict with all the possible trajects as keys and the traject time
    as value

    return  :   dict
    """
    dict_trajects = {}
    G = generate_graph(data)
    for departure_station in get_data.list_of_stations(data):
        for arrival_station in get_data.list_of_stations(data):
            if departure_station != arrival_station:
                for trajects in list(nx.all_simple_paths(G, departure_station, arrival_station)):
                    teller = 0
                    time = 0
                    for i in trajects:
                        if teller < len(trajects)-1 and (i, trajects[teller+1]) in data:
                            time += int(data[(i, trajects[teller+1])])
                            teller += 1
                        elif teller < len(trajects)-1 and (trajects[teller+1], i) in data:
                            time += int(data[(trajects[teller+1], i)])
                            teller += 1

                    if time < (max_time + 1) and tuple(trajects)[::-1] not in dict_trajects:
                        dict_trajects[tuple(trajects)] = time

    return dict_trajects

if __name__ == "__main__":
    G = generate_graph(data.generate_dict()["ConnectiesHolland.csv"])
    print(find_all_trajects(data.generate_dict()["ConnectiesHolland.csv"], 120))
    # plt.figure(1)
    # pos=nx.spring_layout(G)
    # nx.draw_networkx(G, pos)
    # labels = nx.get_edge_attributes(G,'weight')
    # nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    # plt.show()
