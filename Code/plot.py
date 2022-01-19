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
import seaborn as sns

def plot_hist(data):
    l = []
    for i in data[2]:
        l.append(i[1])

    x = np.array(l)

    plt.axvline(data[3], color='red', linewidth=2, label="Mean: " + str(round(data[3], 2)))
    sns.distplot(x, hist = True, kde = True,
                 kde_kws = {'linewidth': 2},
                 label = "Scores")
    plt.xlabel("Score")
    plt.ylabel("fraction of 100.000 tractories")
    plt.title("Scores of trajectories (highest score: " + str(data[1]) + ")")
    plt.legend()
    plt.show()