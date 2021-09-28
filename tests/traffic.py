"""
Name: Tyler McCormack
traffic.py

Problem: This program intakes traffic flow information and outputs individual averages for each road as well as overall averages.

Certificate of Authenticity:
I certify that this is my original work.
"""

def traffic():
    count = 1
    totalNum = 0
    roads = eval(input("How many roads were surveyed? "))
    for i in range(roads):
        days = eval(input("How many days was road " + str(i + 1) + " surveyed? "))
        avgAcc = 0
        for j in range(days):
            numCars = eval(input("How many cars traveled on day " + str(j + 1) + "? "))
            avgAcc = avgAcc + numCars
        avgperDay = avgAcc / days
        print("Road", i + 1, "average vehicles per day:", avgperDay)
        totalNum = totalNum + avgAcc
        avgNum = round(totalNum / roads, 2)
    print("Total number of  vehicles traveled on all roads:", totalNum)
    print("Average number of vehicles per road: ", avgNum)


def main():
    traffic()

if __name__ == '__main__':
    main()