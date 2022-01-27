class Node():
    def __init__(self, name, x, y):
        self.name = name
        self.neighbours = {}
        self.location = (float(x), float(y))

    def add_neighbour(self, neighbour, value):
        self.neighbours[neighbour] = value

    def remove_neighbour(self, neighbour):
        self.neighbours.pop(neighbour)