import numpy as np
with open("week10 unfinished/Nvda_1y_20250305.txt", 'r') as f:
    prices = [float(line.strip()) for line in f]

def moving_average(prices, n):
    first_buy = None
    buy = None
    sell = None
    trade_profit = 0
    total_profit = 0

    for i in range(n,len(prices)-n+1):
        # set condition to buy when holding no stock.
        if buy == None and prices[i] < np.mean(prices[i-n:i])*0.98: # without numpy, use sum(prices[i-n:i])/n
            buy = prices[i]
            print(f'buying at {buy}')
            if first_buy is None:
                first_buy = buy
        elif buy !=None and prices[i] > np.mean(prices[i-n:i])*1.02:
            sell = prices[i]
            trade_profit = sell - buy
            print(f'selling at {sell}')
            print(f'trade profit: {trade_profit:.2f}')
            buy = None # reset buy to None

        total_profit += trade_profit   


    final_profit_percentage = ( total_profit / first_buy ) * 100
    print(f'Total profit: {total_profit:.2f}')
    print(f'fist buy: {first_buy}')
    print(f'% return: {final_profit_percentage:.2f}%')

moving_average(prices, 5)