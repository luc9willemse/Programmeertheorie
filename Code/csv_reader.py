import csv
import os
import ast

def all_trajectories_national():

    path_file = os.path.dirname(os.path.abspath(__file__)) + "/../../All_trajects_nationaal.csv"

    d = {}
    with open(path_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        teller = 0
        for row in csv_reader:
            if teller == 0:
                teller += 1
            else:
                l = ast.literal_eval(row[1])
                d[l] = float(row[2])

    return d