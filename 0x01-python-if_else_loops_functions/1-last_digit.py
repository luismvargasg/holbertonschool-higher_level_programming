#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdig = (number * -1) % 10 * -1
else:
    lastdig = number % 10
str1 = "Last digit of"
str2 = "is"
strgt5 = "and is greater than 5"
striz = "and is 0"
stril6 = "and is less than 6 and not 0"
if lastdig > 5:
    print(str1, number, str2, lastdig, strgt5)
elif lastdig == 0:
    print(str1, number, str2, lastdig, striz)
else:
    print(str1, number, str2, lastdig, stril6)
