"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
from random import randint


def find_and_remove_first(listname, value):
    try:
        i = listname.index(value)
        listname[i] = "Tyler"
    except:
        pass
    print(listname)

def read_data(filename):
    file_name = open(filename, "r")
    data1 = file_name.read()
    data = data1.split()
    return data

def is_in_linear(search_val, values):
    count = 0
    while count < len(values):
        if search_val == eval(values[count]):
            return True
        count += 1
    return False


def good_input():
    num = eval(input("Input a number"))
    iscorrect = False
    while not iscorrect:
        if num < 1:
            print("Too low, pick again")
        elif num > 10:
            print("Too high, pick again")
        elif 1 <= num <= 10:
            iscorrect = True
            break
        num = eval(input("Input a number"))
    if iscorrect:
        print("Input is valid.")
        return num


def num_digits():
    num = eval(input("Enter a number"))
    while num > 0:
        digits = 0
        while num > 0:
            num = num // 10
            digits+=1
        print("Your number had " + str(digits) + " digits")
        num = eval(input("Enter a number"))


def hi_lo_game():
    num = randint(1, 100)
    guesses = 1
    userguess = eval(input("Enter a guess!"))
    while guesses < 7 and not userguess == num:
        guesses += 1
        if userguess > num:
            print("Too high! Guess again." )
        if userguess < num:
            print("Too low! Guess again.")
        userguess = eval(input("Enter a guess!"))
    if guesses >= 7:
        print("You lost. The number was " + str(num))
    elif userguess == num:
        print("You won in " + str(guesses) + " guesses!")

def main():
    # listnames = ["Shannon", "Paul", "Connor", "Jordan", "Eleanor", "Jim"]
    # find_and_remove_first(listnames, "James")
    # listdata = read_data("nums.txt")
    # is_in_linear(3, listdata)
    # good_input()
    # num_digits()
    # hi_lo_game()

if __name__ == '__main__':
    main()
