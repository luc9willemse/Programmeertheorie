"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

plot.py
this file generates a plot of the data
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_hist(data):
    l = []
    for i in data[2]:
        l.append(i[1])

    x = np.array(l)

    plt.hist(x, bins=60)
    plt.xlabel("K (value of objective function)")
    plt.ylabel("Number of tractories")
    plt.title("Number of trajectories with scores (highest score: " + str(data[1]) + ")")
    plt.show()