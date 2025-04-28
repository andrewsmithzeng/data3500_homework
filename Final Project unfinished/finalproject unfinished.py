'''This project is similar to Stock market trading simulations, 
however you will run trading simulations on 6 crypto currencies(not 10) of your choice 
(i.e. bitcoin, bitcoin-cash, ripple, EOS, Litecoin, Ethereum)
Like the stock market project, you will get the price data from a web json API, and save it to csv files.  
An example will be shown in class.
Your program will run two trading strategies(not 3) on the crypto currency prices.
Your program should be able to save new data into the files.  
Meaning, when I go to run your program, it should go get the latest data, update the files, and run new analysis.
If your program detects a buy signal or sell signal on the last day in the data, 
print a message like "You should <buy or sell> this stock today".
Store your results to your strategy in a results.json, 
and specifically identify which crypto currency and strategy made the most profit.
Each project must meet the following 5 project requirements:

Obtaining data from a web JSON API (40 points)
Storing the data in CSV files  (40 points)
The ability to add new data to your dataset.  
Meaning, tomorrow you can run your program again, and it will go get the latest data, and run your analysis again. (40 points)
Perform analysis on the data. (40 points)
Store your results in a results.json file  (40 points)
'''


# Import required libraries
import json
import requests
import time
import numpy as np
from datetime import datetime, timedelta
import os

# Define API keys
key1 = "name"
key2 = "market_data"
key3 = "current_price"
key4 = "usd"

# Define cryptocurrencies to analyze
coins = ["bitcoin"]  # Testing with just bitcoin first

def get_current_price(coin):
    """Get current price for a cryptocurrency"""
    try:
        print(f"Fetching price for {coin}...")
        url = f"https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": coin,
            "vs_currencies": "usd"
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        price = data[coin]["usd"]
        print(f"Current price for {coin}: ${price:,.2f}")
        return price
    except Exception as e:
        print(f"Error getting price for {coin}: {e}")
        return None

def get_historical_prices(coin):
    """Get historical price data for testing"""
    try:
        print(f"Fetching historical data for {coin}...")
        url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"
        params = {
            "vs_currency": "usd",
            "days": "30",  # Get 30 days of hourly data
            "interval": "hourly"
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        prices = []
        for timestamp, price in data["prices"]:
            date = datetime.fromtimestamp(timestamp/1000).strftime("%Y-%m-%d %H:%M:%S")
            prices.append((date, price))
        
        print(f"Got {len(prices)} historical price points")
        return prices
    except Exception as e:
        print(f"Error getting historical data for {coin}: {e}")
        return None

def save_prices(coin, prices):
    """Save multiple price points to CSV file"""
    try:
        filename = f"{coin}.csv"
        
        # Create file with header if it doesn't exist
        if not os.path.exists(filename):
            print(f"Creating new file: {filename}")
            with open(filename, "w") as f:
                f.write("timestamp,price\n")
        
        # Append price data
        print(f"Appending data to {filename}")
        with open(filename, "a") as f:
            for date, price in prices:
                f.write(f"{date},{price}\n")
        
        # Verify file contents
        with open(filename, "r") as f:
            lines = f.readlines()
            print(f"File now contains {len(lines)} lines")
            print("Last line:", lines[-1].strip())
        
        return True
    except Exception as e:
        print(f"Error saving prices for {coin}: {e}")
        print(f"Current working directory: {os.getcwd()}")
        return False

def initial_data_poll(coins):
    """Fetch initial historical data for cryptocurrencies and save to CSV files"""
    for coin in coins:
        print(f"\nFetching data for {coin}...")
        lines = []
        
        try:
            # Use simple price endpoint instead of market_chart
            url = f"https://api.coingecko.com/api/v3/simple/price"
            params = {
                "ids": coin,
                "vs_currencies": "usd",
                "include_24hr_change": "true"
            }
            
            print("Fetching current price data...")
            time.sleep(1)
            
            response = requests.get(url, params=params)
            if response.status_code == 429:  # Rate limit
                print("Rate limit hit, waiting 30 seconds...")
                time.sleep(30)
                response = requests.get(url, params=params)
            
            response.raise_for_status()
            data = response.json()
            
            # Get current price
            current_price = data[coin]["usd"]
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Save to file
            filename = f"{coin}.csv"
            with open(filename, "w") as f:
                f.write(f"{current_time},{current_price}\n")
            print(f"Successfully saved current price to {filename}")
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {coin}: {e}")
        except Exception as e:
            print(f"Unexpected error processing {coin}: {e}")

def append_data(coins):
    """Append new data to existing CSV files"""
    for coin in coins:
        print(f"\nChecking {coin} for new data...")
        
        try:
            # Use simple price endpoint
            url = f"https://api.coingecko.com/api/v3/simple/price"
            params = {
                "ids": coin,
                "vs_currencies": "usd",
                "include_24hr_change": "true"
            }
            
            print("Fetching current price data...")
            time.sleep(1)
            
            response = requests.get(url, params=params)
            if response.status_code == 429:  # Rate limit
                print("Rate limit hit, waiting 30 seconds...")
                time.sleep(30)
                response = requests.get(url, params=params)
            
            response.raise_for_status()
            data = response.json()
            
            # Get current price
            current_price = data[coin]["usd"]
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Append to file
            filename = f"{coin}.csv"
            with open(filename, "a") as f:
                f.write(f"{current_time},{current_price}\n")
            print(f"Successfully appended current price to {filename}")
            
        except Exception as e:
            print(f"Error processing {coin}: {e}")

def mean_reversion_strategy(prices, n=5):
    """Mean reversion trading strategy"""
    first_buy = None
    buy = None
    sell = None
    trade_profit = 0
    total_profit = 0
    buys = []  # 记录买入点
    sells = []  # 记录卖出点

    for i in range(n, len(prices)-n+1):
        # 当没有持仓时，如果价格低于移动平均线的98%，则买入
        if buy is None and prices[i] < np.mean(prices[i-n:i])*0.98:
            buy = prices[i]
            buys.append(i)  # 记录买入位置
            print(f'Buying at ${buy:,.2f}')
            if first_buy is None:
                first_buy = buy
        # 当持有仓位时，如果价格高于移动平均线的102%，则卖出
        elif buy is not None and prices[i] > np.mean(prices[i-n:i])*1.02:
            sell = prices[i]
            sells.append(i)  # 记录卖出位置
            trade_profit = sell - buy
            print(f'Selling at ${sell:,.2f}')
            print(f'Trade profit: ${trade_profit:.2f}')
            buy = None  # 重置买入价格

        total_profit += trade_profit

    # 计算收益率
    if first_buy is not None:
        final_profit_percentage = (total_profit / first_buy) * 100
    else:
        first_buy = 0
        final_profit_percentage = 0

    print(f'Total profit: ${total_profit:.2f}')
    print(f'First buy: ${first_buy:.2f}')
    print(f'Return: {final_profit_percentage:.2f}%')
    
    return {
        "profit": round(total_profit, 2),
        "returns": round(final_profit_percentage, 2),
        "buys": buys,
        "sells": sells
    }

def simple_moving_average(prices, n=5):
    """Simple moving average crossover strategy"""
    first_buy = None
    buy = None
    sell = None
    trade_profit = 0
    total_profit = 0
    buys = []  # 记录买入点
    sells = []  # 记录卖出点

    for i in range(n, len(prices)-n+1):
        # 当没有持仓时，如果价格高于移动平均线，则买入
        if buy is None and prices[i] > np.mean(prices[i-n:i]):
            buy = prices[i]
            buys.append(i)  # 记录买入位置
            print(f'Buying at ${buy:,.2f}')
            if first_buy is None:
                first_buy = buy
        # 当持有仓位时，如果价格低于移动平均线，则卖出
        elif buy is not None and prices[i] < np.mean(prices[i-n:i]):
            sell = prices[i]
            sells.append(i)  # 记录卖出位置
            trade_profit = sell - buy
            print(f'Selling at ${sell:,.2f}')
            print(f'Trade profit: ${trade_profit:.2f}')
            buy = None  # 重置买入价格

        total_profit += trade_profit

    # 计算收益率
    if first_buy is not None:
        final_profit_percentage = (total_profit / first_buy) * 100
    else:
        first_buy = 0
        final_profit_percentage = 0

    print(f'Total profit: ${total_profit:.2f}')
    print(f'First buy: ${first_buy:.2f}')
    print(f'Return: {final_profit_percentage:.2f}%')
    
    return {
        "profit": round(total_profit, 2),
        "returns": round(final_profit_percentage, 2),
        "buys": buys,
        "sells": sells
    }

def calculate_profit(prices, buys, sells):
    """Calculate total profit from buy and sell signals"""
    profit = 0
    for buy in buys:
        for sell in sells:
            if sell > buy:
                profit += prices[sell] - prices[buy]
                break
    return profit

def run_strategies(coin):
    """Run trading strategies on a single coin"""
    try:
        # 读取价格数据
        prices = []
        with open(f"{coin}.csv", "r") as f:
            next(f)  # 跳过标题行
            for line in f:
                price = float(line.strip().split(",")[1])
                prices.append(price)
        
        if len(prices) < 10:  # 确保有足够的数据点
            print(f"Not enough price data for {coin} to run strategies")
            return None
        
        # 运行两个策略
        print(f"\nRunning strategies for {coin}...")
        mr_results = mean_reversion_strategy(prices)
        sma_results = simple_moving_average(prices)
        
        # 返回结果
        return {
            "mean_reversion": mr_results,
            "simple_moving_average": sma_results
        }
        
    except Exception as e:
        print(f"Error running strategies for {coin}: {e}")
        return None

def save_results(results):
    """Save results to JSON file"""
    try:
        with open("results.json", "w") as f:
            json.dump(results, f, indent=4)
        print("\nResults saved to results.json")
    except Exception as e:
        print(f"Error saving results: {e}")

# Main execution
if __name__ == "__main__":
    print("Starting cryptocurrency trading simulation...")
    print(f"Current working directory: {os.getcwd()}")
    
    all_results = {}
    
    # 获取并保存价格数据
    for coin in coins:
        price = get_current_price(coin)
        if price:
            save_prices(coin, get_historical_prices(coin))
    
    # 运行交易策略
    for coin in coins:
        results = run_strategies(coin)
        if results:
            all_results[coin] = results
    
    # 保存结果
    if all_results:
        save_results(all_results)
    
    print("\nDone!")