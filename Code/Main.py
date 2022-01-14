import networkx as nx
import matplotlib.pyplot as plt
import data
import network
import map

if __name__ == "__main__":
    # load data
    All_data = data.Data()
    Network = network.Network()
    Map = map.Map()
    # load Holland
    stations_holland = All_data.stations_holland
    connections_holland = All_data.connecties_holland
    # network
    G = Network.generate_graph(connections_holland)
    print(Network.find_all_trajectories(connections_holland, stations_holland, 120))
    plt.figure(1)
    pos=nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()
    # map
    Map.create_map(stations_holland, connections_holland)
    Map.save_map()