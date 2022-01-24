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
import re

def alg(data, list_of_connections):
    b = False
    score = 0
    trajectories = []
    t = list(data.keys())[random.randint(0,(len(data)-1))]
    trajectories.append(t)
    t = int(data[t])
    while b == False:
        teller = 0
        best_trajectory = []
        for trajectory in data:
            trajectories.append(trajectory)
            #startgrade = time.time_ns()
            g = grade(calc_fraction(trajectories, list_of_connections), len(trajectories), (t + int(data[trajectory])))
            #stopgrade = time.time_ns()
            #print("grade:", stopgrade-startgrade)
            if g > score:
                score = g
                best_time = int(data[trajectory])
                best_trajectory = trajectory
            else:
                teller += 1

            trajectories.remove(trajectory)


        if teller == len(data):
            b = True
        else:
            trajectories.append(best_trajectory)
            t += best_time

    temp_trajectories = trajectories[:]
    for i in range(len(trajectories)):
        b = False
        temp_time = data[temp_trajectories[i]]
        for trajectory in data:
            ti = t
            temp_trajectories[i] = trajectory
            g = grade(calc_fraction(temp_trajectories, list_of_connections), len(temp_trajectories), (ti - temp_time + int(data[trajectory])))
            if g > score:
                score = g
                best_time = ti - temp_time + int(data[trajectory])
                best_trajectory = trajectory
                b = True

        if b == True:
            temp_trajectories[i] = best_trajectory
        else:
            temp_trajectories[i] = trajectories[i]

    trajectories = temp_trajectories

    return (trajectories, best_time, score)

def multi_alg(data, list_of_connections):
    score = 0
    trajectories = []
    time = []
    dict_of_scores = {}
    for i in range(4):
        hc = alg(data, list_of_connections)
        dict_of_scores[tuple(hc[0])] = hc[2]
        if hc[2] > score:
            score = hc[2]
            trajectories = hc[0]
            time = hc[1]

    return (trajectories, time, score, dict_of_scores)


def random_trajectory_generator(data, list_of_connections):
    """
    data    :   datasets (dict of trajects)

    this function picks random trajects

    return  :   list with the randomly chosen trajects, total time of the trajects,
                number of trajects and the fraction of the station that are used
    """
    number_of_trajectories = random.randint(1, 13)
    #number_of_trajectories = 5
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
    return p * 10000 - ((T * 100) + min)


def multiple_random_tractories(data, list_of_connections):
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
    total_grade = 0
    best_time = 0
    t = 10000
    for i in range(t):
        ran = random_trajectory_generator(data, list_of_connections)
        trajectories_and_grades.append((ran[0], round(grade(ran[3], ran[2], ran[1]), 2)))
        g = grade(ran[3], ran[2], ran[1])
        total_grade += g
        if g > beste_grade:
            best_fractions = ran[0]
            beste_grade = grade(ran[3], ran[2], ran[1])
            best_time = ran[1]

    average_grade = total_grade/t

    return (best_fractions, round(beste_grade, 2), trajectories_and_grades, average_grade, best_time)
    #return (round(beste_grade, 2))


def good_trajectories():
    """
    finds what trajects are often found in the combination with a high score
    """
    pass


def good_length_trajectories(data):
    """
    data    :   data with list of tuples, (trajectories, grade)

    finds what length of trajectories is the best, min and max.

    return  :   range of most commen length of trajectories
    """
    l_min = []
    l_max = []
    for trajectory in data:
        if trajectory[1] > 8000:
            trajectory[0].sort(key=lambda t: len(t))
            l_min.append(len(trajectory[0][0]))
            l_max.append(len(trajectory[0][-1]))

    c_min = Counter(l_min)
    c_max = Counter(l_max)

    return (c_min.most_common(1)[0][0], c_max.most_common(1)[0][0])


def best_number_of_trajectories(data):
    """
    data    :   data with list of tuples, (trajectories, grade)

    finds what number of trajectories is the best one

    return  :   most commen number of trajectories
    """
    l = []
    for trajectory in data:
        if trajectory[1] > 8000:
            l.append(len(trajectory[0]))

    c = Counter(l)

    return c.most_common(1)[0][0]

def begin_and_end(data, number_of_trajects):
    """
    data    :   data with list of tuples, (trajectories, grade)

    finds good begin and end stations

    return  :   good begin and end stations
    """
    l = []
    for trajectorys in data:
        if trajectorys[1] > 8000:
            for trajectory in trajectorys[0]:
                l.append(trajectory[0])
                l.append(trajectory[-1])

    l_sort = sorted(l,key=l.count,reverse=True)
    l_sort = list(dict.fromkeys(l_sort))

    return l_sort[0:((number_of_trajects*2)+1)]


def list_of_best_trajectories(data, multi_random):
    """
    data                :   list of all trajectories
    list_of_connections :   list of connections

    this function filters the list of all trajectories

    TODO    :   add more filters

    return  :   filterd list
    """
    d = {}
    length_min = good_length_trajectories(multi_random)[0]
    length_max = good_length_trajectories(multi_random)[1]
    start_station = begin_and_end(multi_random, best_number_of_trajectories(multi_random))
    print(length_min, length_max)
    for trajectorie, grade in data.items():
        if len(trajectorie) - 1 > length_min and len(trajectorie) < length_max + 1 and trajectorie[0] in start_station and trajectorie[-1] in start_station:
            d[trajectorie] = grade

    return d



