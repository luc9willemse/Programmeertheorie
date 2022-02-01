# De Conducteurs

## Project: RailNL

The aim of this project is to design trajectories for the Dutch Railways in a efficient manner. This effectively means that the total time the trains spend in all trajectories should be minimized, while the percentage of connections ridden should be as high as possible. Furthermore, the trajectories are constraint to a pre specified time frame of 2 or 3 hours since longer trajectories aren't feasible in practice. We optimize the following objective function in this project:

#### K = p•10000 - (T•100 + Min)

K: the total combined quality of all trajectories
p: percentage of connections used in all trajectories
T: number of trajectories
Min: total time spend in al trajectories

## Getting Started

### Prerequisites

This project is written in Python3. In the file requirements.txt all packages are shown that are needed to run the code. You can install them easily using the followiing command in the terminal:

```
pip install -r requirements.txt
```

### Structure

* /Code: contains all python code
* /Code/Algorithms: contains code for the different algorithms
* /Code/Classes: contains all classes needed for the project
* /Output/Data: contains the output file with all trajectories and score
* /Output/Maps: contains the maps with all trajectories used
* Output/Plots: contains the plots that shows the results from the algorithms
* /Datasets: contains all csv files needed to run the code
* /Documents: contains the document explaining the results of the different algorithms

### Test (Testing)

To run the code use the following instruction:

```
python3 main.py 
```
This will start up the program's GUI where you can choose how to run the program (National/Holland, Number of iterations, Random/Restart hill climber/Hill climber).

## Authors

* Luc Willemse
* Minne Sandstra
* Stijn Maatje

## Acknowledgments

* StackOverflow
* Networkx developers
* Folium developers

