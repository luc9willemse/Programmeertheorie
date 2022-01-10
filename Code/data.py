"""
Name            :   Luc Willemse
UvAnetID        :   14012391
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
        for row in csv_reader:
            if "Con" in file:
                dictionary[(row[0], row[1])] = row[2]
            else:
                dictionary[row[0]] = (row[1], row[2])

    return dictionary

def generate_dict():
    """
    generates dictionary with al the data sets

    return  :   dict
    """
    dictionary = {}

    datasets = os.listdir(os.path.abspath("Programmeertheorie/Datasets"))
    for file in datasets:
        dictionary[file] = read_data("Programmeertheorie/Datasets/" + file)
    
    return dictionary


if __name__ == "__main__":
    dic = generate_dict()
    print(dic)
