import requests, json, numpy

#stocks to be analyzed
stocks = [
    "AAPL",     # Apple Inc. - Technology
    "MSFT",     # Microsoft Corporation - Technology
    "GOOGL",    # Alphabet Inc. - Technology
    "JPM",      # JPMorgan Chase - Financial
    "BAC",      # Bank of America - Financial
    "WMT",      # Walmart - Retail
    "COST",     # Costco - Retail
    "JNJ",      # Johnson & Johnson - Healthcare
    "UNH",      # UnitedHealth - Healthcare
    "CAT",      # Caterpillar - Industrial
]

# #function 1: pull the initial data from the api and store the open prices in a csv file
# def initial_data_pull(stocks):

#     #construct the url for the api call
#     api_key = "WLHJOGR00DR33F4L"
#     base_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
#     suffix_url = f"&outputsize=full&apikey={api_key}"
#     for stock in stocks:
#         url = base_url + stock + suffix_url
#         #make the api call and convert the response to json
#         data = requests.get(url).json()

#         #create a list to store the open prices
#         open_prices = []
#         #iterate through the data and extract the open prices
#         for date in data["Time Series (Daily)"].keys():
#             open_price = data["Time Series (Daily)"][date]["1. open"] 
#             open_prices.append(f"{stock}, {date}, {open_price}\n")

#         #store the reserverd open_prices list in a csv file
#         with open("Final_Project_unfinished/stock_market_trading/alphavantage/" + stock + "_open_prices.csv", "w") as f:
#             f.writelines(open_prices[::-1])

# #call the initial_data_pull function
# initial_data_pull(stocks)

# #function 2: append the newest data to the csv file
# def append_data(stocks):

#     #construct the url for the api call
#     api_key = "WLHJOGR00DR33F4L"
#     base_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
#     suffix_url = f"&outputsize=full&apikey={api_key}"
#     for stock in stocks:
#         url = base_url + stock + suffix_url
#         #make the api call and convert the response to json
#         data = requests.get(url).json()

#         #get the last day from the csv file
#         with open("Final_Project_unfinished/stock_market_trading/alphavantage/" + stock + "_open_prices.csv", "r") as f:
#             last_day_csv = f.readlines()[-1].split(",")[1].strip()

#         #create a list to store the open prices need to be appended
#         open_prices_to_append = []

#         #iterate through the data and extract the open prices from api
#         for date in data["Time Series (Daily)"].keys():
#             if date == last_day_csv:
#                 break
#             else:
#                 open_price = data["Time Series (Daily)"][date]["1. open"] 
#                 open_prices_to_append.append(f"{stock}, {date}, {open_price}\n")

#     #append the open_prices_to_append to the csv file
#         with open("Final_Project_unfinished/stock_market_trading/alphavantage/" + stock + "_open_prices.csv", "a") as f:
#             f.writelines(open_prices_to_append[::-1])

# #call the append_data function
# append_data(stocks)

#function 3: mean reversion strategy 
def MeanReversionStrategy(prices,n):
    first_buy = None
    buy = None
    sell = None
    trade_profit = 0
    total_profit = 0

    for i in range(n,len(prices)-n+1):
        # set condition to buy when holding no stock.
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
        final_profit_percentage = ( total_profit / first_buy ) * 100
    else:
        first_buy = 0
        final_profit_percentage = 0

    print(f'Total profit: {total_profit:.2f}')
    print(f'First buy: {first_buy}')
    print(f'% return: {final_profit_percentage:.2f}%')
    
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
        # set condition to buy when holding no stock.
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
        final_profit_percentage = ( total_profit / first_buy ) * 100
    else:
        first_buy = 0
        final_profit_percentage = 0

    print(f'Total profit: {total_profit:.2f}')
    print(f'First buy: {first_buy}')
    print(f'% return: {final_profit_percentage:.2f}%')
    
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
        # set condition to buy when holding no stock.
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
        final_profit_percentage = ( total_profit / first_buy ) * 100
    else:
        first_buy = 0
        final_profit_percentage = 0

    print(f'Total profit: {total_profit:.2f}')
    print(f'First buy: {first_buy}')
    print(f'% return: {final_profit_percentage:.2f}%')
    
    bb_profit = round(total_profit,2)
    bb_return = round(final_profit_percentage,2)
    return bb_profit, bb_return

#function 6: check the last day signal
def check_last_day_signal(prices,n):

    last_price = prices[-1]
    mean = numpy.mean(prices[-n:])
    signals = []

    if last_price < mean*0.98:
        signals.append("mean reversion strategy: buy")
    elif last_price > mean*1.02:
        signals.append("mean reversion strategy: sell")

    if last_price > mean:
        signals.append("simple moving average strategy: buy")
    elif last_price < mean:
        signals.append("simple moving average strategy: sell")

    if last_price < mean*0.95:
        signals.append("bollinger bands strategy: buy")
    elif last_price > mean*1.05:
        signals.append("bollinger bands strategy: sell")
        
    return signals

#function 7: save the results to a json file
def SaveResults(dictionary):
    json.dump(dictionary,open('Final_Project_unfinished/stock_market_trading/alphavantage/results.json','w'),indent=4)


#save the results to a dictionary
results = {}
#iterate through the stocks and run the functions
for stock in stocks:
    #isolate the list of prices from the file
    prices = [float(line.split(",")[2].strip()) for line in reversed(list(open('Final_Project_unfinished/stock_market_trading/alphavantage/' + stock + '_open_prices.csv','r')))]
    results[stock+"_prices"]= prices

    # run mean reversion function
    mr_profit,mr_returns =MeanReversionStrategy(prices, 5)
    # get the profit and retun % from the functions and save them to a dictionary
    results[stock+"_mr_profit"]= mr_profit
    results[stock+"_mr_returns"]= mr_returns

    # run simple moving average function
    sma_profit,sma_returns=SimpleMovingAvg(prices, 5)
    # get the profit and retun % from the functions and save them to a dictionary
    results[stock+"_sma_profit"]= sma_profit
    results[stock+"_sma_returns"]= sma_returns

    # run bollinger bands function
    bb_profit,bb_returns=BollingerBandsStrategy(prices, 5)
    # get the profit and retun % from the functions and save them to a dictionary
    results[stock+"_bb_profit"]= bb_profit
    results[stock+"_bb_returns"]= bb_returns

    # check the last day signal
    signals = check_last_day_signal(prices, 5)
    results[stock+"_signals"]= signals

print(results)

# save the results to a json file
SaveResults(results)

'''
missing:
1. If your program detects a buy signal or sell signal on the last day in the data, print a message like “You should <buy or sell> this stock today”.
2. Store your results to your strategy in a results.json, and specifically identify which stock and strategy made the most profit.
'''