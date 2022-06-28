#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    rm = number % 10
else:
    rm = ((number * -1) % 10) * -1
if rm < 6:
	print("Last digit of %d is %d and is less than 6 and not 0"%(number,rm))
elif rm == 0:
	print("Last digit of %d is %d and is 0"%(number,rm))
else:
	print("Last digit of %d is %d and is greater than 5"%(number,rm))
