import json
import os

def MeanReversionStrategy(prices,name):
    pass

def SimpleMovingAvg(prices,name):
    pass

def SaveResults(dictionary):
    json.dump(dictionary,open('week12/HW5/json_files/results.json','w'))

tickers = ['adobe_adbe',pass]

for ticker in tickers:
    #isolate the list of prices from the file
    prices = [float(line) for line in resersed(open('week12/HW5/' + ticker + '_1y_20250404.txt'))]


# run mean reversion and simple moving average
MR_profit,MR_returns =MeanReversionStrategy(prices, ticker)
SMA_profit,SAM_returns=SimpleMovingAvg(prices, ticker)


# get the profit and retun % from the functions and save them to a dictionary
results[ticker+" prices"]= prices
results[ticker+" MR profit"]= MR_profit
results[ticker+" MR returns"]= MR_returns