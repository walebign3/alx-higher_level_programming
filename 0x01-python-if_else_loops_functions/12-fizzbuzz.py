#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i%3 == 0 and i%5 == 0:
            print("{}".format("FizzBuzz"), end=" ")
            continue
        if i%5 == 0:
            print("{}".format("Buzz"), end=" ")
            continue
        if i%3 == 0:
            print("{}".format("Fizz"), end=" ")
            continue
        elif i%3 != 0 and i%5 != 0:
            print("{:d}".format(i), end=" ")
