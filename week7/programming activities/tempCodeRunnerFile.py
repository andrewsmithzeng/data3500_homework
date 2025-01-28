"""
Programming Activity 5.2 
This activity is a continuation from the last one and is meant to help you with your homwork.
Write a Python program to read in the stock prices from a file, into a list.
Create a list of floats from the list of strings you read in, from step 2.
Calculate the average of the first 4 days in your list.
Calculate the average of the last 4 days in your list.
In a for loop, calculate a 4 day moving average for the floats in the list.
Add logic in the for loop to implement a simple moving average 
trading strategy.
Display the profit from the strategy, after the for loop has finished.
"""
import pandas as pd

with open("week7\programming activities\AAPL.2023.txt",'r') as file:
    lines = file.readlines()

entire_values = []
for line in lines:
    entire_values.append(float(line))

moving_average_for_4_days = pd.Series(entire_values).rolling(window=4).mean().dropna().to_list()
print(moving_average_for_4_days)