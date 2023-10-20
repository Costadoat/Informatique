def remove_last_line_from_csv(filename):
    with open(filename) as myFile:
        lines = myFile.readlines()
        last_line = lines[len(lines)-1]
        lines[len(lines)-1] = last_line.rstrip()
    with open('num-points-willie.csv', 'w') as myFile:    
        myFile.writelines(lines)

remove_last_line_from_csv('num-points.csv')

