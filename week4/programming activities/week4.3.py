"""
Programming Activity 3

Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""
for i in range(5,96,5):
    print(i,end = ' ')

for ii in range(1,96):
    if ii % 5 ==0:
        print(ii)