import requests, json
from datetime import datetime
print(datetime.now().strftime('%Y-%m-%d')) #%y：25, %Y:2025

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

#pull the initial data from the api and store the open prices in a csv file
def initial_data_pull(stocks):

    #construct the url for the api call
    api_key = "ACEE72F7S2Z2TN0K"
    base_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
    suffix_url = f"&outputsize=full&apikey={api_key}"
    for stock in stocks:
        url = base_url + stock + suffix_url
        #make the api call and convert the response to json
        data = requests.get(url).json()

        #create a list to store the open prices
        open_prices = ["stock,date,open_price\n"]
        #iterate through the data and extract the open prices
        for date in data["Time Series (Daily)"].keys():
            open_price = data["Time Series (Daily)"][date]["1. open"] 
            open_prices.append(f"{stock}, {date}, {open_price}\n")

        #store the reserverd open_prices list in a csv file
        with open("Final_Project_unfinished/stock_market_trading/alphavantage/" + stock + "_open_prices.csv", "w") as f:
            f.writelines(open_prices[::-1])
            
#call the initial_data_pull function
initial_data_pull(stocks)


            



