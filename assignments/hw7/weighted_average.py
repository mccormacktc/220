"""
Name: Tyler McCormack
weighted_average.py

Problem: This is a program that finds the weighted average of students' work

Certificate of Authenticity:
I certify that this is my original work.
"""
def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w+")
    avgAcc = 0
    x = 0
    for line in in_file:
        name_grade = line.split(":")
        grades = name_grade[1].split(" ")
        grades.pop(0)
        weights = []
        percents = []
        for i in range(len(grades)):
            if i%2 == 0:
                weights.append(grades[i])
            else:
                percents.append(grades[i])
        acc = 0
        weightsum = 0
        for j in range(len(weights)):
            acc = acc + (int(weights[j]) * int(percents[j]))
            weightsum = weightsum + int(weights[j])
        if weightsum != 100 and weightsum > 100:
            out_file.write(name_grade[0] + "'s average: Error: The weights are more than 100.\n")
        elif weightsum != 100 and weightsum < 100:
            out_file.write(name_grade[0] + "'s average: Error: The weights are less than 100.\n")
        else:
            avg = acc / 100
            avgAcc = avg + avgAcc
            out_file.write(name_grade[0] + "'s average: " + str(round(avg, 1)) + "\n")
            x = x + 1
    classavg = round(avgAcc / x, 1)
    out_file.write("Class average: " + str(classavg))
## Lucky Peyton Davidson: 80 12 13 34 1 55 3 68 0 76 0 55 1 41 2 64
## Briana Flaherty: 100 62


# Billy Bother: 20 89 30 94 50 82
# Oh No: 30 52 60 75
# Hermione Heffalump: 40 93 60 97
# Too Bad: 90 95 10 87 20 94
# Kurt The Kidd: 20 88 30 82 40 76 10 99

def main():
    weighted_average("grades.txt", "output.txt")

if __name__ == '__main__':
    main()