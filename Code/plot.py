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


def plot_hist(data, highest_score):

    x = np.array(data)
    sns.distplot(x, hist=True, kde=True,
                 kde_kws={'linewidth': 2},
                 label="Scores")
    plt.xlabel("Score")
    plt.ylabel("fraction of 1000 tractories")
    plt.title("Scores of trajectories (highest score: " + str(highest_score) + ")")
    plt.legend()
    plt.show()
