"""
Programming Activity 5

1. Download one year worth of stock data from yahoo finance. The instructions to do this are in the HW4 description.
2. After you have one year worth of stock data, use a for loop to iterate through the data, 
and calculate the average for the entire data set.
3. After you have calculated the average for the entire data set, 
see if you can calculate the average for the first 5 days only.  
(you will need this logic for your homework).
"""

import pandas as pd

with open("week7\programming activities\AAPL.2023.txt",'r') as file:
    lines = file.readlines()

entire_values = []
for line in lines:
    entire_values.append(float(line))

entire_data_set_average = pd.Series(entire_values).mean()
print("entire_data_set_average:", entire_data_set_average)

first_5_days = []
for i in range(5):
    first_5_days.append(entire_values[i])

first_5_days_average = sum(first_5_days)/len(first_5_days)
print('first_5_days_average:', first_5_days_average)

second_5_days_total= 0
for x in range(5,10):
    second_5_days_total += entire_values[x]
second_5_days_average = second_5_days_total/len(range(5,10))
print(f'second_5_days_average: {second_5_days_average:.5f}')