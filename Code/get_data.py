"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

get_data.py:
this file contains functions that helps you to get easier access to the data
"""
import data

def connected_stations(data, max):
    """
    data    :   dataset
    max     :   the max time of a traject

    this function creates a list of lists, the lists contain trajects that take
    less time than the max time

    return  :   list of lists
    """
    list_of_trajects = []
    for connection in list_of_connected_stations(data):
        traject = [connection[0], connection[1]]
        station = connection[1]
        time = int(data[(connection[0], connection[1])])
        while time < max:
            teller = 0
            for i in list_of_connected_stations(data):
                if i[0] == station and i[1] not in traject:
                    traject.append(i[1])
                    time += int(data[(station, i[1])])
                    station = i[1]
                    print(traject, time)
                elif i[1] == station and i[0] not in traject:
                    traject.append(i[0])
                    time += int(data[(i[0], station)])
                    station = i[0]
                    print(traject, time)
                else:
                    teller += 1

            if teller == len(list_of_connected_stations(data)):
                break

        traject.pop()
        list_of_trajects.append(traject)

    return list_of_trajects


def list_of_connected_stations(data):
    """
    data    :   dataset

    this function modifies the normal dataset to a list with only the connections

    return  :   list of tuples
    """
    l = []
    for connection in data:
        l.append(connection)
    return l

def list_of_stations(data):
    """
    data    :   dataset

    this function gives a list with al the stations

    return  :   list
    """
    l = []
    for connections in list_of_connected_stations(data):
        if connections[0] not in l:
            l.append(connections[0])
        if connections[1] not in l:
            l.append(connections[1])

    return l

if __name__ == "__main__":
    print(list_of_stations(data.generate_dict()["ConnectiesHolland.csv"]))



