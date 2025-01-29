"""
Programming Activity 5.2 
This activity is a continuation from the last one and is meant to help you with your homwork.
Write a Python program to read in the stock prices from a file, into a list.
Create a list of floats from the list of strings you read in, from step 2.
Calculate the average of the first 4 days in your list.
Calculate the average of the last 4 days in your list.
In a for loop, calculate a 4 day moving average for the floats in the list.
Add logic in the for loop to implement a simple moving average trading strategy.
Display the profit from the strategy, after the for loop has finished.
"""

import pandas as pd

#必须indent，在文件打开的情况下，才能读取
with open("week7\programming activities\AAPL.2023.txt",'r') as file:
    lines = file.readlines()

#convert lines into floats and insert them into a new list
#solution 1:
# entire_prices = []
# for price in lines:
#     entire_prices.append(float(price))
#solution 2:
entire_prices = [float(price.strip()) for price in lines]

# average for the first four days 
first_four_avg = sum(entire_prices[:4])/4
print("first_four_avg:", first_four_avg)

# average for the last four days 
last_four_avg = sum(entire_prices[-4:])/4
print("last_four_avg:", last_four_avg)

# average for the 4 days of moving average
moving_average_for_4_days = pd.Series(entire_prices).rolling(window=4).mean().to_list()
print(moving_average_for_4_days)


#in for price < avg and out for price > avg
buy = None
total_profit = 0
for ID, price in enumerate(entire_prices): 
    # solution 1:
    # if ID < 3 :
    #     continue
    #solution 2:
    if pd.isna(moving_average_for_4_days[ID]):
        continue


    else :
        if price < moving_average_for_4_days[ID] and buy is None:
            buy = price
            print(f'buying at date {ID}, price: {price}')
        elif price > moving_average_for_4_days[ID] and buy is not None:
            print(f'Selling at date {ID}, price: {price}, profit: {price - buy}')
            total_profit += (price - buy)
            buy = None


# if there is still a position on the last day, force a closing selling
if buy is not None:
    total_profit += (entire_prices[-1]-buy)
    print(f'Final sell at last day {len(entire_prices)}, price: {entire_prices[-1]}, profit: {entire_prices[-1]-buy}')

print(f'total_profit is {total_profit}')