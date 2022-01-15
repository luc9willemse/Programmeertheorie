"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

data.py:
Generates a dictionairy with the names of different datasets as the key and
the actual data as the value.
"""

import csv
import os

def read_data(file):
    """
    file    :   csv file

    converts a csv file to a dictionary

    return  :   dict
    """
    dictionary = {}

    with open(file, "r") as f:
        csv_reader = csv.reader(f, delimiter=',')
        teller = 0
        for row in csv_reader:
            if teller == 0:
                teller += 1
            else:
                if "tiesHo" in file:
                    dictionary[(row[0], row[1])] = row[2]
                elif "tiesNa" in file:
                    dictionary[(row[0], row[1])] = float(row[2])
                else:
                    dictionary[row[0]] = (row[1], row[2])

    return dictionary

def generate_dict():
    """
    generates dictionary with al the data sets

    return  :   dict
    """
    dictionary = {}
    path_file = os.path.dirname(os.path.abspath(__file__)) + '/'
    datasets = os.listdir(path_file + "../Datasets")
    for file in datasets:
        dictionary[file] = read_data(path_file + "../Datasets/" + file)

    return dictionary

