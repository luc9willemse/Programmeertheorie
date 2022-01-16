"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

data.py:
this file contains functions that helps you to get easier access to the data
"""
import load_data

class Data():
    # get loaded data
    def __init__(self):
        self.dict = load_data.generate_dict()
        self.connecties_holland = self.dict["ConnectiesHolland.csv"]
        self.connecties_nationaal = self.dict["ConnectiesNationaal.csv"]
        self.stations_holland = self.list_of_stations(self.connecties_holland)
        self.stations_nationaal = self.list_of_stations(self.connecties_nationaal)

    # def connected_stations(data, max):
    #     """
    #     data    :   dataset
    #     max     :   the max time of a trajectory

    #     this function creates a list of lists, the lists contain trajectories that take
    #     less time than the max time

    #     return  :   list of lists
    #     """
    #     list_of_trajectories = []
    #     for connection in list_of_connected_stations(data):
    #         trajectory = [connection[0], connection[1]]
    #         station = connection[1]
    #         time = int(data[(connection[0], connection[1])])
    #         while time < max:
    #             teller = 0
    #             for i in list_of_connected_stations(data):
    #                 if i[0] == station and i[1] not in trajectory:
    #                     trajectory.append(i[1])
    #                     time += int(data[(station, i[1])])
    #                     station = i[1]
    #                     print(trajectory, time)
    #                 elif i[1] == station and i[0] not in trajectory:
    #                     trajectory.append(i[0])
    #                     time += int(data[(i[0], station)])
    #                     station = i[0]
    #                     print(trajectory, time)
    #                 else:
    #                     teller += 1

    #             if teller == len(list_of_connected_stations(data)):
    #                 break

    #         trajectory.pop()
    #         list_of_trajectories.append(trajectory)

    #     return list_of_trajectories

    def list_of_connected_stations(self, data):
        """
        data    :   dataset

        this function modifies the normal dataset to a list with only the connections

        return  :   list of tuples
        """
        l = []
        for connection in data:
            l.append(connection)
        return l

    def list_of_stations(self, data):
        """
        data    :   dataset
        this function gives a list with al the stations
        return  :   list
        """
        l = []
        for connections in self.list_of_connected_stations(data):
            if connections[0] not in l:
                l.append(connections[0])
            if connections[1] not in l:
                l.append(connections[1])

        return l

if __name__ == "__main__":
    data = Data()
    print(data.stations_holland)