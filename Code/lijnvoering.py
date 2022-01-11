"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

lijnvoering.py:
this file contains the algoritems that find the lijnvoering
"""
import data
import network
import random
import get_data
from collections import Counter

def random_traject_generater(data):
    """
    data    :   datasets (dict of trajects)

    this function picks random trajects

    return  :   list with the randomly chosen trajects, total time of the trajects,
                number of trajects and the fraction of the station that are used
    """
    #number_of_trajects = random.randint(1, 7)
    number_of_trajects = 5
    list_of_traject = []
    total_time = 0
    for i in range(number_of_trajects):
        traject = list(data.keys())[random.randint(0,(len(data)-1))]
        list_of_traject.append(traject)
        total_time += int(data[traject])

    teller = 0
    list_of_stations = get_data.list_of_stations(data)
    for traject in list_of_traject:
        for station in traject:
            if station in list_of_stations:
                teller += 1
                list_of_stations.remove(station)

    fraction = teller / len(get_data.list_of_stations(data))

    return [list_of_traject, total_time, number_of_trajects, fraction]

def grade(p, T, min):
    """
    p   :   fraction of the total stations
    T   :   number of trajects
    min :   total min of the trajects

    grades the the chosen trajects

    return  :   int
    """
    return p * 10000 - (T * 100 + min)

def best_trajects(data):
    """
    data    :   dataset

    runs the random fraction generator multiple times and picks the best one,
    also keeps track of al the scores.

    return  :   list with the best combination of fractions found, the best
                grade and a list of all the grades
    """
    trajects_grades = []
    best_fractions = []
    beste_grade = 0
    for i in range(10000):
        ran = random_traject_generater(data)
        trajects_grades.append((ran[0], round(grade(ran[3], ran[2], ran[1]), 2)))
        if grade(ran[3], ran[2], ran[1]) > beste_grade:
            best_fractions = ran[0]
            beste_grade = grade(ran[3], ran[2], ran[1])

    return (best_fractions, round(beste_grade, 2), trajects_grades)

def good_trajects():
    """
    finds what trajects are often found in the combination with a high score
    """
    pass

def best_number_of_trajects(data):
    """
    finds what number of trajects is the best one
    """
    l = []
    for traject in data:
        if traject[1] > 8000:
            l.append(len(traject[0]))

    c = Counter(l)

    return c.most_common(1)

if __name__ == "__main__":
    ran = random_traject_generater(network.find_all_trajects(data.generate_dict()["ConnectiesHolland.csv"], 120))
    best = best_trajects(network.find_all_trajects(data.generate_dict()["ConnectiesHolland.csv"], 120))
    best_num = best_number_of_trajects(best[2])
    print(best[1])
