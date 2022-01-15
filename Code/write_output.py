import csv

def write_output(solution):
    """
    write a csv file with the solution
    """
    f = open('Output/Data/output.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['train', 'stations'])
    for i in range(len(solution[0])):
        writer.writerow(['train_' + str(i+1), solution[0][i]])
    writer.writerow(['score', solution[1]])
    f.close()