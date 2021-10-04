"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter a first and last name").split(" ")
    print(name[1] + ", " + name[0])

def company_name():
    website = input("Enter a three-part internet domain name").split(".")
    print(website[1])

def initials():
    numstudents = eval(input("How many names will you input?"))
    for i in range(numstudents):
        firstname = input("Enter the first name of student " + str(i+1) + ":")
        lastname = input("Enter " + firstname + "'s last name:")
        print(firstname + "'s initials are " + firstname[0] + lastname[0])

def names():
    names = input("Enter a list of names separated by commas").split(", ")
    print("The initials are", end=" ")
    for i in range(len(names)):
        splitnames = names[i].split(" ")
        firstname = splitnames[0]
        lastname = splitnames[1]
        setinitials = firstname[0] + lastname[0]
        print(setinitials, end=" ")


def thirds():
    numsentences = eval(input("Enter the number of sentences: "))
    for i in range(numsentences):
        sentence = input("Enter a sentence")
        print(sentence[2:len(sentence):3])

def word_average():
    sentence = input("Enter a sentence").split(" ")
    acc = 0
    for i in range(len(sentence)):
        acc = acc + len(sentence[i])
    wrdavg = acc / len(sentence)
    print(wrdavg)

def pig_latin():
    sentence = input("Enter a sentence").lower()
    sentence = sentence.split(" ")
    for word in sentence:
        print(word[1:] + word[0] + "ay", end=" ")

def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
    # add other function calls here


main()
