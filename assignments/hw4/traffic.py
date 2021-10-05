"""
Name: Tyler McCormack
traffic.py

Problem: This program intakes traffic flow information and outputs individual averages for each
road as well as overall averages.

Certificate of Authenticity:
I certify that this is my original work.
"""

def traffic():
    totalnum = 0
    roads = eval(input("How many roads were surveyed? "))
    for i in range(roads):
        days = eval(input("How many days was road " + str(i + 1) + " surveyed? "))
        avgacc = 0
        for j in range(days):
            numcars = eval(input("How many cars traveled on day " + str(j + 1) + "? "))
            avgacc = avgacc + numcars
        avgperday = round(avgacc / days, 2)
        print("Road", i + 1, "average vehicles per day:", avgperday)
        totalnum = totalnum + avgacc
        avgnum = round(totalnum / roads, 2)
    print("Total number of  vehicles traveled on all roads:", totalnum)
    print("Average number of vehicles per road: ", avgnum)


def main():
    traffic()

if __name__ == '__main__':
    main()
