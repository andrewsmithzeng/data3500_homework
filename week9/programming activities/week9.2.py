"""
Programming Activity 2

Create a NumPy array of 100 numbers, initialized to 0. 
Then, change the array from 0s to random numbers.
"""

import numpy as np
import random

arr = np.zeros(100)
print(arr)

lst = [random.randint(0,100) for x in range(100)]
arr = np.array(lst)
print(arr)