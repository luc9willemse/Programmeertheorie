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
    # restartHC = RestartHC(graph)
    # solution = restartHC.test()

    # generate a random solution
    #all_trajectories = graph.find_all_trajectories(120)
    # print(all_trajectories[('Alkmaar', 'Den Helder')])
    all_trajectories = all_trajectories_national()
    # print(all_trajectories[('Alkmaar', 'Den Helder')])

    #l_all_random = lv.multiple_random_tractories(all_trajectories, graph.list_of_connections())
    start = time.time()
    #hill = lv.hill_climb(all_trajectories, graph.list_of_connections())
    m_alg = lv.multi_alg(all_trajectories, graph.list_of_connections())
    #backtrack = lv.backtrakking(graph.dic_of_connections())
    stop = time.time()
    print(m_alg[0], m_alg[1], m_alg[2])
    print(stop-start)
    write_output(m_alg, m_alg[2], m_alg[1])
    map = Map(graph.nodes, graph.dic_of_connections(), type)
    map.add_solution(m_alg[0])
    map.save_map()

    # # write final output

    #plot_hist(m_alg)
    # best = lv.best_trajectories(all_trajectories, graph.list_of_nodes())
    # plot_hist(best)
    # plt.figure(1)
    # pos=nx.spring_layout(graph)
    # nx.draw_networkx(graph, pos)
    # labels = nx.get_edge_attributes(graph,'weight')
    # nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
    # plt.show()