"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

main.py
"""
from importlib.resources import path
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
import webbrowser
import os

welcome_text = ("\n"
                "Dit het project van Stijn Maatje, Minne Sandstra en Luc Willemse. Dit \n" +
                "Project heet RailNl. Het doel van die project is trajecten vormen voor \n" +
                "de Nederlande spoorwegen. Om dit doel te bereiken hebben wij verschillende \n" +
                "algoritmes verzonnen. Kies eerst of je de spoorwegen van alleen Holland wil \n" +
                "zien of de spoorwegen van heel Nederland. Type: \n" +
                " - Holland \n" +
                " - Nationaal \n")

regio_text = ("Type 'menu' om de verschillende algoritmes te zien. \n")

menu = ("\n" +
        "Welkom bij ons keuzemenu, u kunt keuze maken uit de volgende algoritmes: \n")

alg_options = ( " - Random \n" +
                " - Hill Climb \n" +
                " - Restart Hill Climb \n" +
                "type quit of het menu te verlaten. \n")

random_text = ( "Welkom bij ons random algoritme, dit algoritme pakt random trajecten en berekend \n" +
                "daar de score van. Dit algoritme doet dat 100.000 keer. Dit duurt ongeveer 2 min, \n" +
                "dus pak lekker wat koffie dan is die klaar wanneer je terug bent.")
vervolg_random_text = ( "Hoe is de koffie? het rekenen is klaar. Er zijn verschillende dingen die \n" +
                        "je over dit algoritme kan bekijken, wanneer je quit in typed verlaat je \n" +
                        "dit algoritme. \n")

hill_climb_text_Holland = ( "Welkom bij ons hill climb algoritme, dit algoritme begint bij een random traject. \n" +
                            "Dan gaat die alle trajecten langs en voegt ze toe om te kijken of daardoor de \n" +
                            "score omhoog gaat. Dit blijft die doen totdat dit niet meer het geval is. Daarna \n" +
                            "haalt die het eerst toegevoegde traject weg en gaat kijken of er een ander traject \n" +
                            "zorgt voor een betere score. Dit blijft die doen totdat alle traject weer gecontroleerd \n" +
                            "zijn. Dit algoritme runnen we 100 keer en dan komt er eigenlijk altijd dezelfde score uit. \n" +
                            "Dit kan even duren. \n")
vervolg_hill_climb_text_Holland = ( "Het rekenen is klaar. Er zijn verschillende dingen die je over \n" +
                                    "dit algoritme kan bekijken, wanneer je quit in typed verlaat je \n" +
                                    "dit algoritme. \n")

hill_climb_text_Nationaal = (   "Welkom bij ons hill climb algoritme, dit algoritme begint bij een random traject. \n" +
                                "Dan gaat die alle trajecten langs en voegt ze toe om te kijken of daardoor de \n" +
                                "score omhoog gaat. Dit blijft die doen totdat dit niet meer het geval is. Daarna \n" +
                                "haalt die het eerst toegevoegde traject weg en gaat kijken of er een ander traject \n" +
                                "zorgt voor een betere score. Dit blijft die doen totdat alle traject weer gecontroleerd \n" +
                                "zijn. Dit algoritme runnen we 1 keer en dan komt dus niet altijd op dezelfde score uit. \n" +
                                "Dit kan even duren. \n")
vervolg_hill_climb_text_Nationaal = (   "Het rekenen is klaar. Er zijn verschillende dingen die je over \n" +
                                        "dit algoritme kan bekijken, wanneer je quit in typed verlaat je \n" +
                                        "dit algoritme. \n")
restart_hill_climb_text = ("")

print(welcome_text)
b = False
while b == False:
    size = input()
    if size == "Holland":
        graph = Graph(size)
        print(regio_text)
        break
    elif size == "Nationaal":
        graph = Graph(size)
        print(regio_text)
        break
    else:
        print(  "Wat u heeft ingetypt was geen optie, de opties zijn: \n" +
                " - Holland \n" +
                " - Nationaal \n")

b = False
while b == False:
    x = input()
    if x == "menu":
        print(menu)
        break
    else:
        print(  "Wat u heeft ingetypt was geen optie, de opties zijn: \n" +
                " - menu \n")

b = False
while b == False:
    print(alg_options)
    x = input()
    if x == "Random":
        print(random_text)
        ran = randomAlgoritme(graph)
        multi_random = ran.multiple_random_tractories()
        print(vervolg_random_text)
        p = False
        while p == False:
            print( "Opties zijn: \n" +
                        " - plot \n" +
                        " - map \n" +
                        " - trajecten \n" +
                        " - score \n" +
                        " - time \n" +
                        " - quit \n")
            x = input()
            if x == "plot":
                plot_hist(multi_random[2], multi_random[1])
            elif x == "map":
                map = Map(graph.nodes, graph.dic_of_connections(), size)
                map.add_solution(multi_random[0])
                map.save_map()
                url = os.path.dirname(os.path.abspath(__file__))[0:-8] + '/Output/Maps/' + size + 'Map.html'
                print(os.getcwd())
                filename = 'file:///' + os.getcwd() + '/Output/Maps/' + size + 'Map.html'
                webbrowser.open_new_tab(filename)
            elif x == "trajecten":
                print(multi_random[0], "\n")
            elif x == "score":
                print(multi_random[1], "\n")
            elif x == "time":
                print(multi_random[4], "\n")
            elif x == "quit":
                break
    elif x == "Hill Climb" and size == "Holland":
        print(hill_climb_text_Holland)
        hc = hillClimb(graph)
        hill_climb = hc.multi_alg(100)
        print(vervolg_hill_climb_text_Holland)
        p = False
        while p == False:
            print( "Opties zijn: \n" +
                        " - plot \n" +
                        " - map \n" +
                        " - trajecten \n" +
                        " - score \n" +
                        " - time \n" +
                        " - quit \n")
            x = input()
            if x == "plot":
                plot_hist(hill_climb[3], hill_climb[2])
            elif x == "map":
                map = Map(graph.nodes, graph.dic_of_connections(), size)
                map.add_solution(hill_climb[0])
                map.save_map()
                url = os.path.dirname(os.path.abspath(__file__))[0:-8] + '/Output/Maps/' + size + 'Map.html'
                print(os.getcwd())
                filename = 'file:///' + os.getcwd() + '/Output/Maps/' + size + 'Map.html'
                webbrowser.open_new_tab(filename)
            elif x == "trajecten":
                print(hill_climb[0], "\n")
            elif x == "score":
                print(hill_climb[2], "\n")
            elif x == "time":
                print(hill_climb[1], "\n")
            elif x == "quit":
                break
    elif x == "Hill Climb" and size == "Nationaal":
        print(hill_climb_text_Nationaal)
        hc = hillClimb(graph)
        hill_climb = hc.multi_alg(1)
        print(vervolg_hill_climb_text_Nationaal)
        p = False
        while p == False:
            print( "Opties zijn: \n" +
                        " - plot \n" +
                        " - map \n" +
                        " - trajecten \n" +
                        " - score \n" +
                        " - time \n" +
                        " - quit \n")
            x = input()
            if x == "plot":
                plot_hist(hill_climb[3], hill_climb[2])
            elif x == "map":
                map = Map(graph.nodes, graph.dic_of_connections(), size)
                map.add_solution(hill_climb[0])
                map.save_map()
                url = os.path.dirname(os.path.abspath(__file__))[0:-8] + '/Output/Maps/' + size + 'Map.html'
                print(os.getcwd())
                filename = 'file:///' + os.getcwd() + '/Output/Maps/' + size + 'Map.html'
                webbrowser.open_new_tab(filename)
            elif x == "trajecten":
                print(hill_climb[0], "\n")
            elif x == "score":
                print(hill_climb[2], "\n")
            elif x == "time":
                print(hill_climb[1], "\n")
            elif x == "quit":
                break
    elif x == "Restart Hill Climb":
        print(restart_hill_climb_text)
    elif x == quit:
        break
    else:
        print(  "Wat u heeft ingetypt was geen optie, de opties zijn: \n")
