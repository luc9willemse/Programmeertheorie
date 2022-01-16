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
import Code.Algorithms.lijnvoering as lv
from Code.write_output import write_output
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or (sys.argv[1] != 'Holland' and sys.argv[1] != 'Nationaal'):
        sys.exit("Usage: python3 Main.py Holland/Nationaal")
    type = sys.argv[1]
    graph = Graph(type)

    all_trajectories = graph.find_all_trajectories(120)
    solution = lv.random_trajectory_generator(all_trajectories, graph.list_of_connections())
    print(solution[3], solution[2], solution[1])
    grade = lv.grade(solution[3], solution[2], solution[1])
    print(grade)
    map = Map(graph.nodes, graph.dic_of_connections(), type)
    map.add_solution(solution)
    map.save_map()
    write_output(solution, grade)

    # best = lv.best_trajectories(all_trajectories, graph.list_of_nodes())
    # plot_hist(best)
    # plt.figure(1)
    # pos=nx.spring_layout(graph)
    # nx.draw_networkx(graph, pos)
    # labels = nx.get_edge_attributes(graph,'weight')
    # nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
    # plt.show()