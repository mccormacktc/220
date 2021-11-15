"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
from random import randint

def main():
    # add other function calls here
    play()


def listwords(in_file_name):
    in_file = open(in_file_name, "r")
    return in_file.readlines()


def wordpicker(lst):
    wordnum = randint(0, (len(lst) - 1))
    return lst[wordnum]


def fill(word, lstletters):
    secret = ['_'] * len(word)
    for letter in lstletters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)


def won(word, lstletters):
    x = fill(word, lstletters)
    if word == x:
        return True
    else:
        return False


def play():
    words = listwords("wordlist.txt")
    secret = wordpicker(words)
    incorrect = 0
    guesses = []
    current = ['_'] * len(secret)
    while not(won(secret, guesses)) and incorrect < 7:
        # display = fill(secret, guesses)
        print(guesses)
        for char in current:
            print(char, end="")
        print("\n")
        letter = input()
        while letter in guesses:
            letter = input()
        guesses.append(letter)
        display = fill(secret, guesses)
        if not(letter in secret):
            incorrect += 1
        else:
            current = display
            for char in current:
                print(char, end="")
            print("\n")

    if won(secret, guesses):
        print("Congrats! You won!")
    elif incorrect == 7:
        print("You lost :(")

main()
