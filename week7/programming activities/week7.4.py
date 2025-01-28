"""
Programming Activity 4 

Using the list you generated in programming activity 3, extend your program to check if there are 2 even numbers in a row. 
If there are two even numbers in a row, print the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number and next number are both even.
"""

import random
lst = []
for i in range(10):
    lst.append(random.randint(1,5))
print(lst)

found_pair = False
for count in range(len(lst)):
    if lst[count-1] %2 == 0 and  lst[count] % 2 == 0:
      print(f'there are 2 even numbers in a row and they are {lst[count-1]} & {lst[count]} in position {count-1} & {count}')
      found_pair = True
    
if not found_pair:
    print('there are no 2 even numbers in a row.')