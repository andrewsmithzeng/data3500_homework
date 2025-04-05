import os, pandas, numpy, json


#function 1: extract the closing prices from the csv files and save them to their corresponding txt files, all at once.
def convert_clomn_to_text(folder_panth):
    for filename in os.listdir(folder_panth):
        if filename.endswith('.csv'):
            csv_path = os.path.join(folder_panth, filename)
            column = pandas.read_csv(csv_path,usecols=['Close/Last'])
            values = column['Close/Last'].iloc[1:].str.replace('$','',regex = False).astype(float)

            txt_filename = filename.replace('.csv', '.txt')
            txt_path = os.path.join(folder_panth, txt_filename)

            with open(txt_path, 'w') as txt_file:
                for value in values:
                    txt_file.write(f"{value}\n")
#call the function 1 to convert the csv files to txt files
# convert_clomn_to_text('week12\HW5')


#function 2: mean reversion strategy 
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

#function 3: simple moving average strategy
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


    pass


#function 4: save the results to a json file
def SaveResults(dictionary):
    json.dump(dictionary,open('week12/HW5/results.json','w'),indent=4)

#save the results to a dictionary
results = {}
tickers = ['adbe','goog','googl','aapl','fis','fi','intu','pypl','hood','sofi','sqcc']
for ticker in tickers:
    #isolate the list of prices from the file
    prices = [float(line) for line in reversed(list(open('week12/HW5/' + ticker + '_1y_20250404.txt','r')))]
    results[ticker+"_prices"]= prices

    # run mean reversion function
    mr_profit,mr_returns =MeanReversionStrategy(prices, 5)
    # get the profit and retun % from the functions and save them to a dictionary
    results[ticker+"_mr_profit"]= mr_profit
    results[ticker+"_mr_returns"]= mr_returns

    # run simple moving average function
    sma_profit,sma_returns=SimpleMovingAvg(prices, 5)
    # get the profit and retun % from the functions and save them to a dictionary
    results[ticker+"_sma_profit"]= sma_profit
    results[ticker+"_sma_returns"]= sma_returns
print(results)

# save the results to a json file
SaveResults(results)




