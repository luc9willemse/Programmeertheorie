#from Classes.graph import Graph
import random

class RestartHC:
    def __init__(self, Graph):
        self.graph = Graph
        self.number_of_trajects = 5

        if self.graph.size == 'Holland':
            self.time_limit = 120
        else:  # Nationaal
            self.time_limit = 180

    def starting_connections(self):
        return random.choices(self.graph.list_of_connections(), k=self.number_of_trajects)

    def grade(self, solution):
        """
        p   :   fraction of the total stations
        T   :   number of trajects
        min :   total min of the trajects

        grades the the chosen trajects

        return  :   int
        """
        total_time = 0
        connections_used = set()
        stations = self.graph.nodes
        for traject in solution:
            for i in range(len(traject)-2):
                if not ((traject[i], traject[i+1]) in connections_used or (traject[i+1], traject[i]) in connections_used):
                    connections_used.add((traject[i], traject[i+1]))
                    total_time += stations[traject[i]].neighbours[traject[i+1]]

        fraction = len(connections_used) / self.graph.number_of_connections
        return fraction * 10000 - self.number_of_trajects * 100 - total_time
    
    def get_time(self, traject):
        total_time = 0
        for i in range(len(traject)-2):
            total_time += self.graph.nodes[traject[i]].neighbours[traject[i+1]]
        return total_time
    
    def add_best_connection(self, solution):
        best_solution = solution
        best_grade = -10000

        for i in range(self.number_of_trajects):
            traject = list(solution[i])
            last_station = traject[-1]
            first_station = traject[0]

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
                        traject_time = self.get_time(new_traject)

                        if self.get_time(new_traject) <= self.time_limit:
                            new_grade = self.grade(new_solution)

                    if new_grade > best_grade:
                        best_solution = new_solution
                        best_grade = new_grade

        return best_solution, best_grade

    def run(self):
        solution = self.starting_connections()
        best_solution = solution
        best_grade = self.grade(best_solution)
        N = 0
        while N < 100:
            new_solution, new_grade = self.add_best_connection(best_solution)
            if new_grade > best_grade:
                best_solution = new_solution
                best_grade = new_grade
            else:
                N += 1
        return best_grade, best_solution

    def test(self):
        best_grade = -10000
        best_solution = []
        for i in range(5000):
            new_grade, new_solution = self.run()
            if new_grade > best_grade:
                best_grade = new_grade
                best_solution = new_solution
        return best_grade, best_solution