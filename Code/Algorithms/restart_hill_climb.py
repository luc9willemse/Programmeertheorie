import random

class RestartHC:
    def __init__(self, Graph, number_of_trajectories):
        self.graph = Graph
        self.number_of_trajects = number_of_trajectories

        if self.graph.size == 'Holland':
            self.time_limit = 120
        else:  # Nationaal
            self.time_limit = 180

    def starting_connections(self):
        """
        get k random starting connections

        return  :   list of k connections
        """
        return random.choices(self.graph.list_of_connections(), k=self.number_of_trajects)

    def grade(self, solution):
        """
        solution    :   a solution (i.e. lijnvoering) consisting of a list of trajects

        grades the solution

        return  :   float
        """
        total_time = 0
        connections_used = set()
        stations = self.graph.nodes

        # iterate over all trajects and all connections in these trajects
        for traject in solution:
            for i in range(len(traject)-2):
                # check if connection (a,b) or (b,a) is already used
                if not ((traject[i], traject[i+1]) in connections_used or (traject[i+1], traject[i]) in connections_used):
                    connections_used.add((traject[i], traject[i+1]))
                    total_time += stations[traject[i]].neighbours[traject[i+1]]

        fraction = len(connections_used) / self.graph.number_of_connections
        return fraction * 10000 - self.number_of_trajects * 100 - total_time

    def get_time(self, traject):
        """
        traject    :   list

        calculates total time of a traject

        return  :   float
        """
        total_time = 0
        for i in range(len(traject)-2):
            total_time += self.graph.nodes[traject[i]].neighbours[traject[i+1]]
        return total_time

    def add_best_connection(self, solution):
        """
        solution    :   list of lists (list of trajects)

        picks the connection to add to the traject which yields the highest increase in score

        best_solution   :   list of lists (list of trajects with best connection added)
        best_grade      :   grade corresponding to best_solution
        """
        best_solution = solution
        # best_grade is initially set to a number which will always be lower than any grade
        best_grade = -10000

        for i in range(self.number_of_trajects):
            traject = list(solution[i])
            last_station = traject[-1]
            first_station = traject[0]

            # check at the beginning and end of a traject
            for current_station in [last_station, first_station]:
                for neighbour in self.graph.nodes[current_station].neighbours:
                    new_solution = solution[:]
                    new_traject = traject[:]
                    new_grade = -10000

                    # checks stations at the end of the traject
                    if current_station == last_station and neighbour != new_traject[-2]:
                        new_traject.append(neighbour)
                        new_solution[i] = new_traject

                        if self.get_time(new_traject) <= self.time_limit:
                            new_grade = self.grade(new_solution)

                    # checks stations at the beginning of the traject
                    elif current_station == first_station and neighbour != new_traject[1]:
                        new_traject.insert(0, neighbour)
                        new_solution[i] = new_traject

                        if self.get_time(new_traject) <= self.time_limit:
                            new_grade = self.grade(new_solution)

                    # check if solution has improved
                    if new_grade > best_grade:
                        best_solution = new_solution
                        best_grade = new_grade

        return best_solution, best_grade

    def run(self):
        """
        run the algorithm once

        best_solution   :   list of lists (list of trajects with best connection added)
        best_grade      :   grade corresponding to best_solution
        """
        # get initial starting connections
        solution = self.starting_connections()
        best_solution = solution
        best_grade = self.grade(best_solution)
        N = 0

        # if no connection has been added after 100 times, terminate the algorithm
        while N < 100:
            new_solution, new_grade = self.add_best_connection(best_solution)

            # check if solution has improved
            if new_grade > best_grade:
                best_solution = new_solution
                best_grade = new_grade
            else:
                N += 1
        return best_grade, best_solution

    def test(self):
        """
        run the algorithm multiple times

        best_solution   :   list of lists (list of trajects with best connection added)
        best_grade      :   grade corresponding to best_solution
        """
        best_grade = -10000
        best_solution = []

        # run the algorithm 5000 times
        for i in range(5000):
            new_grade, new_solution = self.run()

            # check if new_solution is the best one yet
            if new_grade > best_grade:
                best_grade = new_grade
                best_solution = new_solution
        return best_grade, best_solution