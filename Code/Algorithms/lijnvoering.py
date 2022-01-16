"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

lijnvoering.py:
this file contains the algoritems that find the lijnvoering
"""
import random
from collections import Counter

def random_trajectory_generator(data, list_of_connections):
    """
    data    :   datasets (dict of trajects)

    this function picks random trajects

    return  :   list with the randomly chosen trajects, total time of the trajects,
                number of trajects and the fraction of the station that are used
    """
    number_of_trajectories = random.randint(1, 7)
    list_of_trajectories = []
    total_time = 0
    for i in range(number_of_trajectories):
        traject = list(data.keys())[random.randint(0,(len(data)-1))]
        list_of_trajectories.append(traject)
        total_time += int(data[traject])

    fraction = calc_fraction(list_of_trajectories, list_of_connections)

    return [list_of_trajectories, total_time, number_of_trajectories, fraction]


def calc_fraction(list_of_trajectories, list_of_connections):
    """
    list_of_trajectories    :   list of the trajectories
    list_of_connection      :   list of all the connections

    this function calculates what fraction of the connections are used by the trajectories

    return  :   fraction
    """
    l = []
    for trajectorie in list_of_trajectories:
        for i in range(len(trajectorie)-1):
            if (trajectorie[i], trajectorie[i+1]) not in l and (trajectorie[i+1], trajectorie[i]) not in l:
                l.append((trajectorie[i], trajectorie[i+1]))

    return len(l) / len(list_of_connections)


def grade(p, T, min):
    """
    p   :   fraction of the total stations
    T   :   number of trajects
    min :   total min of the trajects

    grades the the chosen trajects

    return  :   int
    """
    return p * 10000 - (T * 100 + min)


def best_trajectories(data, list_of_stations):
    """
    data    :   dataset

    runs the random fraction generator multiple times and picks the best one,
    also keeps track of al the scores.

    return  :   list with the best combination of fractions found, the best
                grade and a list of all the grades
    """
    trajectories_and_grades = []
    best_fractions = []
    beste_grade = 0
    for i in range(10000):
        ran = random_trajectory_generator(data, list_of_stations)
        trajectories_and_grades.append((ran[0], round(grade(ran[3], ran[2], ran[1]), 2)))
        if grade(ran[3], ran[2], ran[1]) > beste_grade:
            best_fractions = ran[0]
            beste_grade = grade(ran[3], ran[2], ran[1])

    return (best_fractions, round(beste_grade, 2), trajectories_and_grades)
    #return (round(beste_grade, 2))


def good_trajectories():
    """
    finds what trajects are often found in the combination with a high score
    """
    pass


def good_number_trajectories(data):
    """
    finds what length of trajectories is the best, min and max.
    """
    l_min = []
    l_max = []
    for trajectory in data:
        if trajectory[1] > 8500:
            trajectory[1].sort()
            l_min = trajectory[1][0]
            l_max = trajectory[1][-1]

    c_min = Counter(l_min)
    c_max = Counter(l_max)

    return (c_min.most_common(1)[0][0], c_max.most_common(1)[0][0])


def best_number_of_trajectories(data):
    """
    finds what number of trajectories is the best one
    """
    l = []
    for trajectory in data:
        if trajectory[1] > 8500:
            l.append(len(trajectory[0]))

    c = Counter(l)

    return c.most_common(1)[0][0]
