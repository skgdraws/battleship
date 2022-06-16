from csv import *

def read_lines(save):
    
    matrix_pos = open(f"assets/data/save{save}/game.txt", 'r')
    linea = matrix_pos.readlines()
    matrix = []
    for col in linea:
        for row in col:
            print(row)
            line = []

            if row == "5":
                line.append(5)
            elif row == "1":
                line.append(1)
            elif row == "2":
                line.append(2)
            elif row == "3":
                line.append(3)

        matrix.append(line)
    print(matrix)
    return matrix

def import_scores(path):
    score_list = []
    # Opening up the csv File
    with open(path) as map:

        scores = reader(map, delimiter = ',')
        for row in scores:
            score_list.append(list(row))
            
        return score_list

def save_data(score, name):
    file = open('assets/data/scores.csv', "a", newline="")

    data = (score, name)
    data_writer = writer(file)
    data_writer.writerow(data)
    file.close()

read_lines(1)