import os,pandas, numpy, json

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

convert_clomn_to_text('week12\HW5')

with open("week10/Nvda_1y_20250305.txt", 'r') as f:
    prices = [float(line) for line in f]
def MeanReversionStrategy(prices,name):
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


    final_profit_percentage = ( total_profit / first_buy ) * 100
    print(f'Total profit: {total_profit:.2f}')
    print(f'fist buy: {first_buy}')
    print(f'% return: {final_profit_percentage:.2f}%')



def SimpleMovingAvg(prices, n,name):
   

moving_average(prices, 5)

    pass

def SaveResults(dictionary):
    json.dump(dictionary,open('week12/HW5/json_files/results.json','w'))



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