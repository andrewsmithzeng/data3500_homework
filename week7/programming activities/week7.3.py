"""
Programming Activity 3

Create a list that stores 10 random integers. Start with an empty list, then use the append(), 
and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""
import random
lst = []
for i in range(10):
    lst.append(random.randint(1,5))
print(lst)