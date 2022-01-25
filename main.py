"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

main.py
"""
from os import name
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes import graph
from Code.Classes.graph import Graph
from Code.Classes.map import Map
from Code.plot import plot_hist
import Code.Algorithms.lijnvoering as lv
from Code.write_output import write_output
import sys
import time
from Code.csv_reader import all_trajectories_national
from Code.Algorithms.restart_hill_climb import RestartHC

if __name__ == "__main__":
    # checks if proper amount and type of arguments are given in command line
    if len(sys.argv) != 2 or (sys.argv[1] != 'Holland' and sys.argv[1] != 'Nationaal'):
        sys.exit("Usage: python3 main.py Holland/Nationaal")

    # create Graph instance
    type = sys.argv[1]
    graph = Graph(type)

    # Restart Hill Climb algorithm
    start = time.time()
    restartHC = RestartHC(graph)
    solution = restartHC.test()
    stop = time.time()

    # generate a random solution
    #all_trajectories = graph.find_all_trajectories(120)
    # print(all_trajectories[('Alkmaar', 'Den Helder')])
    #all_trajectories = all_trajectories_national()
    # print(all_trajectories[('Alkmaar', 'Den Helder')])

    #l_all_random = lv.multiple_random_tractories(all_trajectories, graph.list_of_connections())
    
    #hill = lv.hill_climb(all_trajectories, graph.list_of_connections())
    #m_hill = lv.multi_hill_climb(all_trajectories, graph.list_of_connections())
    
    #m_hill = lv.multi_hill_climb(all_trajectories, graph.list_of_connections())
    #print(l_all_random)
    print(stop-start)
    map = Map(graph.nodes, graph.dic_of_connections(), type)
    map.add_solution(solution[1])
    map.save_map()
    print(solution)

    # # write final output
    #write_output(l_all_random, l_all_random[1], l_all_random[4])
    #plot_hist(l_all_random)
    # best = lv.best_trajectories(all_trajectories, graph.list_of_nodes())
    # plot_hist(best)
    # plt.figure(1)
    # pos=nx.spring_layout(graph)
    # nx.draw_networkx(graph, pos)
    # labels = nx.get_edge_attributes(graph,'weight')
    # nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
    # plt.show()