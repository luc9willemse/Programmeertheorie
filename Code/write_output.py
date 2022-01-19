import csv

def write_output(solution, grade, time):
    """
    write a csv file with the solution
    """
    # open file to write in
    f = open('Output/Data/output.csv', 'w')
    writer = csv.writer(f)

    # write header
    writer.writerow(['train', 'stations'])

    # write data
    for i in range(len(solution[0])):
        writer.writerow(['train_' + str(i+1), solution[0][i]])

    # write final information
    writer.writerow(['Total time: ' + str(time)])
    writer.writerow(["Score: " + str(round(grade, 2))])

    # close file
    f.close()