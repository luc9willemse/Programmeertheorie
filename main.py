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
from Code.write_output import write_output
import sys
import time
from Code.csv_reader import all_trajectories_national
from Code.Algorithms.restart_hill_climb import RestartHC
from Code.Algorithms.hill_climb import hillClimb
from Code.Algorithms.random_algorithm import randomAlgoritme

if __name__ == "__main__":
    # checks if proper amount and type of arguments are given in command line
    if len(sys.argv) != 2 or (sys.argv[1] != 'Holland' and sys.argv[1] != 'Nationaal'):
        sys.exit("Usage: python3 main.py Holland/Nationaal")

    # create Graph instance
    type = sys.argv[1]
    print(type)
    graph = Graph(type)

    # Restart Hill Climb algorithm
    # start = time.time()
    # restartHC = RestartHC(graph)
    # solution = restartHC.test()
    # stop = time.time()

    # hill = hillclimb(graph)
    # print(hill.multi_alg())
    # ran = randomAlgoritme(graph)
    # print()
    # generate a random solution
    #all_trajectories = graph.find_all_trajectories(120)
    #print(all_trajectories[('Alkmaar', 'Hoorn', 'Zaandam', 'Castricum', 'Alkmaar', 'Den Helder')])
    #all_trajectories = all_trajectories_national()
    # print(all_trajectories[('Alkmaar', 'Den Helder')])
    #graph.load_connections()
    #l_all_random = lv.multiple_random_tractories(all_trajectories, graph.list_of_connections())
    # start = time.time()
    # # #hill = lv.alg(all_trajectories, graph.list_of_connections())
    #m_alg = lv.multi_alg(all_trajectories, graph.list_of_connections())
    # # # #backtrack = lv.backtrakking(graph.dic_of_connections())
    # # stop = time.time()
    # print(m_alg[0], m_alg[1], m_alg[2])
    # # print(stop-start)
    map = Map(graph.nodes, graph.dic_of_connections(), type)
    map.add_solution(ran.multiple_random_tractories())
    map.save_map()
    # # print(m_alg)

    # # # write final output
    # write_output(m_alg, m_alg[2], m_alg[1])
    plot_hist(m_alg)
    # best = lv.best_trajectories(all_trajectories, graph.list_of_nodes())
    # plot_hist(best)
    # plt.figure(1)
    # pos=nx.spring_layout(graph)
    # nx.draw_networkx(graph, pos)
    # labels = nx.get_edge_attributes(graph,'weight')
    # nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
    # plt.show()