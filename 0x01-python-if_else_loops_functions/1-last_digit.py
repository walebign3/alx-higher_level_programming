#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rm = number % 10
if rm < 6:
	print("Last digit of {} is {} and is less than 6 and not 0".format(number,rm))
elif rm == 0:
	print("Last digit of {} is {} and is 0".format(number,rm))
else:
	print("Last digit of {} is {} and is greater than 5".format(number,rm))
