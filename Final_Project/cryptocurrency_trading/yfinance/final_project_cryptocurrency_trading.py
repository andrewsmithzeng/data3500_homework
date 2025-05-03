import yfinance as yf
import pandas as pd
import numpy
import json


# Define cryptocurrencies to analyze
coins = [
    "BTC-USD",          # Bitcoin - The largest cryptocurrency by market cap
    "ETH-USD",         # Ethereum - The second largest cryptocurrency
    "BNB-USD",      # Binance Coin - Binance's native token
    "ADA-USD",          # Cardano - Smart contract platform
    "SOL-USD",           # Solana - High-performance blockchain
    "DOGE-USD",         # Dogecoin - Popular meme cryptocurrency
]

#function 1: pull the initial data from the api and store the open prices in a csv file
def initial_data_pull(coins):
    for coin in coins:
        data = yf.download(
            coin,
            period = 'max',
            interval = '1d'
        )['Open',coin]

        open_prices = [f'{coin}, {date.strftime("%Y-%m-%d")}, {value}\n'
                    for date, value in data.items()]
        
        #store the reserverd open_prices list in a csv file
        with open("Final_Project/cryptocurrency_trading/yfinance/" + coin + "_open_prices.csv", "w") as f:
            f.writelines(open_prices)

# #call the initial_data_pull function
initial_data_pull(coins)

#function 2: append the newest data to the csv file
def append_data(coins):

    for coin in coins:
        data = yf.download(
            coin,
            period = '3mo',
            interval = '1d'
        )['Open',coin]

        #get the last day from the csv file
        with open("Final_Project/cryptocurrency_trading/yfinance/" + coin + "_open_prices.csv", "r") as f:
            last_day_csv = f.readlines()[-1].split(",")[1].strip()

        #create a list to store the open prices need to be appended
        open_prices_to_append = []

        #iterate through the data and extract the open prices to append
        for date, value in list(data.items())[::-1]:
            if date.strftime("%Y-%m-%d") == last_day_csv:
                break
            else:
                open_prices_to_append.append(f'{coin}, {date.strftime("%Y-%m-%d")}, {value}\n')

    #append the open_prices_to_append to the csv file
        with open("Final_Project/cryptocurrency_trading/yfinance/" + coin + "_open_prices.csv", "a") as f:
            f.writelines(open_prices_to_append[::-1])

#call the append_data function
append_data(coins)

#function 3: mean reversion strategy 
def MeanReversionStrategy(prices,n):
    first_buy = None
    buy = None
    sell = None
    trade_profit = 0
    total_profit = 0

    for i in range(n,len(prices)-n+1):
        # set condition to buy when holding no coin.
        if buy == None and prices[i] < numpy.mean(prices[i-n:i])*0.98: # without numpy, use sum(prices[i-n:i])/n
            buy = prices[i]
            print(f'buying at {buy}')
            if first_buy is None:
                first_buy = buy
        elif buy !=None and prices[i] > numpy.mean(prices[i-n:i])*1.02:
            sell = prices[i]
            trade_profit = sell - buy
            print(f'selling at {sell}')
            print(f'trade profit: {trade_profit:.2f}')
            buy = None # reset buy to None

        total_profit += trade_profit   
     # in case there is no buy at all   
    if first_buy is not None:
        final_profit_percentage = ( total_profit / first_buy ) 
    else:
        first_buy = 0
        final_profit_percentage = 0

    print(f'Total profit: {total_profit:.2f}')
    print(f'First buy: {first_buy}')
    print(f'Return: {final_profit_percentage:.2f}')
    
    mr_profit = round(total_profit,2)
    mr_return = round(final_profit_percentage,2)
    return mr_profit, mr_return

#function 4: simple moving average strategy
def SimpleMovingAvg(prices, n):
    first_buy = None
    buy = None
    sell = None
    trade_profit = 0
    total_profit = 0

    for i in range(n,len(prices)-n+1):
        # set condition to buy when holding no coin.
        if buy == None and prices[i] > numpy.mean(prices[i-n:i]): # without numpy, use sum(prices[i-n:i])/n
            buy = prices[i]
            print(f'buying at {buy}')
            if first_buy is None:
                first_buy = buy
        elif buy !=None and prices[i] < numpy.mean(prices[i-n:i]):
            sell = prices[i]
            trade_profit = sell - buy
            print(f'selling at {sell}')
            print(f'trade profit: {trade_profit:.2f}')
            buy = None # reset buy to None

        total_profit += trade_profit   

     # in case there is no buy at all   
    if first_buy is not None:
        final_profit_percentage = ( total_profit / first_buy ) 
    else:
        first_buy = 0
        final_profit_percentage = 0

    print(f'Total profit: {total_profit:.2f}')
    print(f'First buy: {first_buy}')
    print(f'Return: {final_profit_percentage:.2f}')
    
    sma_profit = round(total_profit,2)
    sma_return = round(final_profit_percentage,2)
    return sma_profit, sma_return

#function 5: bollinger bands strategy 
def BollingerBandsStrategy(prices,n):
    first_buy = None
    buy = None
    sell = None
    trade_profit = 0
    total_profit = 0

    for i in range(n,len(prices)-n+1):
        # set condition to buy when holding no coin.
        if buy == None and prices[i] < numpy.mean(prices[i-n:i])*0.95: # without numpy, use sum(prices[i-n:i])/n
            buy = prices[i]
            print(f'buying at {buy}')
            if first_buy is None:
                first_buy = buy
        elif buy !=None and prices[i] > numpy.mean(prices[i-n:i])*1.05:
            sell = prices[i]
            trade_profit = sell - buy
            print(f'selling at {sell}')
            print(f'trade profit: {trade_profit:.2f}')
            buy = None # reset buy to None

        total_profit += trade_profit   
     # in case there is no buy at all   
    if first_buy is not None:
        final_profit_percentage = ( total_profit / first_buy ) 
    else:
        first_buy = 0
        final_profit_percentage = 0

    print(f'Total profit: {total_profit:.2f}')
    print(f'First buy: {first_buy}')
    print(f'Return: {final_profit_percentage:.2f}')
    
    bb_profit = round(total_profit,2)
    bb_return = round(final_profit_percentage,2)
    return bb_profit, bb_return

#function 6: check the last day signal
def check_last_day_signal(prices,n):

    last_price = prices[-1]
    mean = numpy.mean(prices[-n:])
    signals = []

    #mean reversion strategy signal
    if last_price < mean*0.98:
        signals.append(f"based on the mean reversion strategy: you should BUY {coin} coin today")
    elif last_price > mean*1.02:
        signals.append(f"based on the mean reversion strategy: you should SELL {coin} coin today")

    #simple moving average strategy signal
    if last_price > mean:
        signals.append(f"based on the simple moving average strategy: you should BUY {coin} coin today")
    elif last_price < mean:
        signals.append(f"based on the simple moving average strategy: you should SELL {coin} coin today")

    #bollinger bands strategy signal
    if last_price < mean*0.95:
        signals.append(f"based on the bollinger bands strategy: you should BUY {coin} coin today")
    elif last_price > mean*1.05:
        signals.append(f"based on the bollinger bands strategy: you should SELL {coin} coin today")

    print(signals)
    return signals

#function 7: save the results to a json file
def SaveResults(dictionary):
    json.dump(dictionary,open('Final_Project/cryptocurrency_trading/yfinance/results.json','w'),indent=4)


#save the results to a dictionary
results = {}
#iterate through the stocks and run the functions
for coin in coins:
    #isolate the list of prices from the file
    prices = [float(line.split(",")[2].strip()) for line in reversed(list(open('Final_Project/cryptocurrency_trading/yfinance/' + coin + '_open_prices.csv','r')))]
    
    # run mean reversion function
    mr_profit,mr_returns =MeanReversionStrategy(prices, 5)
    # get the profit and retun from the functions and save them to a dictionary
    results[coin+"_mr_profit"]= mr_profit
    results[coin+"_mr_returns"]= mr_returns

    # run simple moving average function
    sma_profit,sma_returns=SimpleMovingAvg(prices, 5)
    # get the profit and retun from the functions and save them to a dictionary
    results[coin+"_sma_profit"]= sma_profit
    results[coin+"_sma_returns"]= sma_returns

    # run bollinger bands function
    bb_profit,bb_returns=BollingerBandsStrategy(prices, 5)
    # get the profit and retun from the functions and save them to a dictionary
    results[coin+"_bb_profit"]= bb_profit
    results[coin+"_bb_returns"]= bb_returns

    # run the check_last_day_signal function
    signals = check_last_day_signal(prices, 5)
    results[coin+"_signals"]= signals

    #specify the strategy for each coin that made the highest return
    if mr_returns > sma_returns and mr_returns > bb_returns:
        results[coin+"_best_strategy"]= "mean reversion strategy"
    elif sma_returns > mr_returns and sma_returns > bb_returns:
        results[coin+"_best_strategy"]= "simple moving average strategy"
    else:
        results[coin+"_best_strategy"]= "bollinger bands strategy"

#specify the coin that made the highest return
most_profitable_coin = ""
highest_return = float('-inf')
for k,v in results.items():
    if k.endswith("_returns"):
        if v > highest_return:
            highest_return = v
            most_profitable_coin = k.split("_")[0]

results["Most_profitable_coin"] = most_profitable_coin
results["Highest_return"] = highest_return

print(results)

# save the results to a json file
SaveResults(results)