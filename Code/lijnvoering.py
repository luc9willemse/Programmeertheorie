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

def random_traject_generater(data):
    """
    data    :   datasets (dict of trajects)

    this function picks random trajects
    """
    number_of_trajects = random.randint(1, 7)
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
    return p * 10000 - (T * 100 + min)

def best_trajects(data):
    best_fractions = []
    beste_grade = 0
    for i in range(10000):
        ran = random_traject_generater(data)
        if grade(ran[3], ran[2], ran[1]) > beste_grade:
            best_fractions = ran[0]
            beste_grade = grade(ran[3], ran[2], ran[1])

    return (best_fractions, beste_grade)



if __name__ == "__main__":
    ran = random_traject_generater(network.find_all_trajects(data.generate_dict()["ConnectiesHolland.csv"], 120))
    best = best_trajects(network.find_all_trajects(data.generate_dict()["ConnectiesHolland.csv"], 120))
    print(best)
