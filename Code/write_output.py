import csv

def write_output(solution, grade):
    """
    write a csv file with the solution
    """
    f = open('Output/Data/output.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['train', 'stations'])
    for i in range(len(solution[0])):
        writer.writerow(['train_' + str(i+1), solution[0][i]])
    writer.writerow(['Total time: ' + str(solution[1])])
    writer.writerow(["Score: " + str(round(grade, 2))])
    f.close()