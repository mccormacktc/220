"""
Name: Tyler McCormack
Partner: <your partner's name goes here – first and last>
lab7.py
"""
from math import pi
def cash_conversion():
    moneyinput = eval(input("Enter an integer"))
    print('${:.2f}'.format(moneyinput))

def encode():
    primarymsg = input("Enter your message")
    for x in primarymsg:
        newval = ord(x) + 3
        print(chr(newval), end ="")
    print(" ")

def sphere_area(radius):
    surface_area = 4 * pi * radius ** 2
    return surface_area

def sphere_volume(radius):
    volume = (4 / 3) * pi * radius ** 3
    return volume

def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    return acc

def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + i ** 3
    return acc

def encode_better():
    message = input("Enter your message")
    cipher = input("Enter a cipher word")
    acc = ''
    for i in range(len(message)):
        char = ord(message[i])
        key = ord(cipher[i])
        newcharord = char + key - 97
        acc += chr(newcharord)
        #print(chr(newcharord), end="")
    print(acc)

def main():
    cash_conversion()
    encode()
    print(sphere_area(2))
    print(sphere_volume(2))
    print(sum_n(4))
    print(sum_n_cubes(4))
    encode_better()
    pass

if __name__ == '__main__':
    main()
