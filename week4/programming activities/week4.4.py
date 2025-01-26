"""
Programming Activity 4

Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
"""
a = 0
while a < 94:
    a +=5
    print(a)

b = 1
while b < 96:
    b += 1
    if b % 5 == 0:
        print(b)