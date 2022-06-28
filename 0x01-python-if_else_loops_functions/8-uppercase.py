#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            capl = ord(letter) - 32
        else:
            capl = ord(letter)
        print("{:c}".format(capl), end='')
    print('\n')
