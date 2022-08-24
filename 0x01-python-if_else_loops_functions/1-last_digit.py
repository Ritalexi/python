#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
import math
last_digit = math.fmod(number, 10)
last_digit = math.floor(last_digit)
last_digit = number % 10
if (last_digit > 5):
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif (last_digit == 0):
    print("Last digit of", number, "is", last_digit, "and is 0")
elif (last_digit < 6 & last_digit != 0):
    print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
