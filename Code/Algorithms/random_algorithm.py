import random


class randomAlgoritme:
    def __init__(self, Graph):
        self.graph = Graph

        if self.graph.size == 'Holland':
            self.time_limit = 120
        else:  # Nationaal
            self.time_limit = 180

    def random_trajectory_generator(self, data, list_of_connections):
        """
        data    :   datasets (dict of trajectories)

        this function picks random trajectories

        return  :   list with the randomly chosen trajectories, total time of the trajectories,
                    number of trajectories and the fraction of the station that are used
        """
        number_of_trajectories = random.randint(1, 13)
        list_of_trajectories = []
        total_time = 0
        for i in range(number_of_trajectories):
            traject = list(data.keys())[random.randint(0, (len(data)-1))]
            list_of_trajectories.append(traject)
            total_time += int(data[traject])

        fraction = self.calc_fraction(list_of_trajectories, list_of_connections)

        return [list_of_trajectories, total_time, number_of_trajectories, fraction]

    def calc_fraction(self, list_of_trajectories, list_of_connections):
        """
        list_of_trajectories    :   list of the trajectories
        list_of_connection      :   list of all the connections

        this function calculates what fraction of the connections are used by the trajectories

        return  :   fraction
        """
        list = []
        for trajectory in list_of_trajectories:
            for i in range(len(trajectory)-1):
                if (trajectory[i], trajectory[i+1]) not in list and (trajectory[i+1], trajectory[i]) not in list:
                    list.append((trajectory[i], trajectory[i+1]))

        return len(list) / len(list_of_connections)

    def grade(self, p, T, min):
        """
        p   :   fraction of the total stations
        T   :   number of trajectories
        min :   total min of the trajectories

        grades the the chosen trajectories

        return  :   int
        """
        return p * 10000 - ((T * 100) + min)

    def multiple_random_tractories(self):
        """
        data    :   dataset

        runs the random fraction generator multiple times and picks the best one,
        also keeps track of al the scores.

        return  :   list with the best combination of fractions found, the best
                    grade and a list of all the grades
        """
        data = self.graph.find_all_trajectories(self.time_limit)
        list_of_connections = self.graph.list_of_connections()
        grades = []
        best_fractions = []
        beste_grade = 0
        total_grade = 0
        best_time = 0
        t = 100000
        for i in range(t):
            ran = self.random_trajectory_generator(data, list_of_connections)
            grades.append(round(self.grade(ran[3], ran[2], ran[1]), 2))
            g = self.grade(ran[3], ran[2], ran[1])
            total_grade += g
            if g > beste_grade:
                best_fractions = ran[0]
                beste_grade = self.grade(ran[3], ran[2], ran[1])
                best_time = ran[1]

        average_grade = total_grade/t

        return (best_fractions, round(beste_grade, 2), grades, average_grade, best_time)
