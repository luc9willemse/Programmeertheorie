"""
Name            :   Luc Willemse, Minne Sandstra, Stijn Maatje
UvAnetID        :   14012391, 12261440, 12276529
Project group   :   10
Programmeertheorie

plot.py
this file generates a plot of the data
"""
import lijnvoering
import data
import network
import matplotlib.pyplot as plt
import numpy as np

def plot_hist(data):
    l = []
    for i in data[2]:
        l.append(i[1])

    x = np.array(l)

    plt.hist(x, bins=60, label="tract combinations grades")
    plt.xlabel("grade")
    plt.ylabel("number of track combinations")
    plt.title("traction combinations grades, highest grade: " + str(data[1]))
    plt.legend()
    plt.show()

if __name__ == "__main__":
    best = lijnvoering.best_trajectories(network.find_all_trajectories(data.generate_dict()["ConnectiesHolland.csv"], 120))
    plot_hist(best)
