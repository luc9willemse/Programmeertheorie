import random
from collections import Counter
import re

class hillClimb:
    def __init__(self, Graph):
        self.graph = Graph

        if self.graph.size == 'Holland':
            self.time_limit = 120
        else:  # Nationaal
            self.time_limit = 180


    def calc_fraction(self, list_of_trajectories, list_of_connections):
        """
        list_of_trajectories    :   list of the trajectories
        list_of_connection      :   list of all the connections

        this function calculates what fraction of the connections are used by the trajectories

        return  :   fraction
        """
        l = []
        for trajectory in list_of_trajectories:
            for i in range(len(trajectory)-1):
                if (trajectory[i], trajectory[i+1]) not in l and (trajectory[i+1], trajectory[i]) not in l:
                    l.append((trajectory[i], trajectory[i+1]))

        return len(l) / len(list_of_connections)


    def grade(self, p, T, min):
        """
        p   :   fraction of the total stations
        T   :   number of trajectories
        min :   total min of the trajectories

        grades the the chosen trajectories

        return  :   int
        """
        return p * 10000 - ((T * 100) + min)

    def alg(self, data, list_of_connections):
        b = False
        score = 0
        trajectories = []
        t = list(data.keys())[random.randint(0,(len(data)-1))]
        #t = ("Heerlen", "Sittard", "Maastricht")
        trajectories.append(t)
        t = int(data[t])
        while b == False:
            teller = 0
            best_trajectory = []
            for trajectory in data:
                trajectories.append(trajectory)
                g = self.grade(self.calc_fraction(trajectories, list_of_connections), len(trajectories), (t + int(data[trajectory])))
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
                g = self.grade(self.calc_fraction(temp_trajectories, list_of_connections), len(temp_trajectories), (ti - temp_time + int(data[trajectory])))
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

    def multi_alg(self, number):
        data = self.graph.find_all_trajectories(self.time_limit)
        list_of_connections = self.graph.list_of_connections()
        score = 0
        trajectories = []
        time = []
        list_of_scores = []
        for i in range(number):
            hc = self.alg(data, list_of_connections)
            list_of_scores.append(hc[2])
            if hc[2] > score:
                score = hc[2]
                trajectories = hc[0]
                time = hc[1]

        return (trajectories, time, score, list_of_scores)
