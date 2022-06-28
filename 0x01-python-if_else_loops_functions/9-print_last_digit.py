#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        rm = number % 10
    else:
        rm = (number % -10)*-1
    print("{}".format(rm), end='')
    return rm
