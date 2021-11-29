"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
from graphics import Rectangle


def is_in_binary(search_val, values):
    midpoint = values[len(values) // 2]
    while midpoint != search_val and len(values) != 1:
        if search_val > midpoint:
            values = values[midpoint:]
        else:
            values = values[:midpoint]
        midpoint = values[len(values) // 2]
    if len(values) == 1 and values[0] != search_val:
        return False
    else: return True

def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i + 1, len(values)):
            if values[j] < values[i]:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]

def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy

def rect_sort(rects):
    dict = {}
    areas = []
    for rect in rects:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rects[i] = dict[areas[i]]

def star_find(filename):
    file = open(filename, "r")
    signals = file.read().split()
    found = []
    beforefive = 0
    for i in range(len(signals)):
        beforefive += 1
        if 4000 < int(signals[i]) < 5000:
            found.append(eval(signals[i]))
        if len(found) >= 5:
            print("Had to search " + str(beforefive) + " before five signals were found!")
            print("Found " + str(len(found)) + " pulses")
            break
    if len(found) < 5:
        print("No neutron stars found. " + str(beforefive) + "signals were searched.")
def main():
    star_find("signals.txt")

if __name__ == '__main__':
    main()
