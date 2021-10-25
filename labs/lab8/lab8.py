"""
Name: Tyler McCormack
lab8.py
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w+")
    i = 1
    for line in in_file:
        words = line.split()
        for word in words:
            out_file.write(str(i) + " " + word + "\n")
            i += 1
    in_file.close()
    out_file.close()

def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w+")
    for line in in_file:
        parts = line.split()
        wage = float(parts[2])
        wage += 1.65
        wage = str(round(wage * int(parts[3]), 2))
        out_file.write(parts[0] + " " + parts[1] + " " + wage + "\n")

def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        position = 10 - i
        acc += int(isbn[i]) * position
    print(acc)

def send_message(file, friend):
    in_file = open(file, "r")
    out_file = open(friend + ".txt", "w+")
    for line in in_file:
        out_file.write(line)

def send_safe_message (in_file_name, friend, key):
    in_file = open(in_file_name, "r")
    out_file = open(friend + ".txt", "w+")
    for line in in_file:
        out_file.write(encode(line, key))

def send_uncrackable_message(in_file_name, friend, pad):
    padfile = open(pad, "r")
    key = padfile.read()
    in_file = open(in_file_name, "r")
    out_file = open(friend + ".txt", "w+")
    for line in in_file:
        out_file.write(encode_better(line, key))

def main():
    number_words("Walrus.txt", "Wout.txt")
    hourly_wages("hourly_wages.txt", "newpay.txt")
    calc_check_sum("0072946520")
    send_message("message.txt", "Ashley")
    send_safe_message("secret_message.txt", "Katie", 4)
    send_uncrackable_message("secret_message.txt", "Aliece", "pad.txt")

main()
