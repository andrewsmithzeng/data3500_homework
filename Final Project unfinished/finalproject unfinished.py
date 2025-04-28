# Import required libraries
import json
import requests
import time
import numpy as np
from datetime import datetime
import os

# Define cryptocurrencies to analyze
coins = [
    "bitcoin",          # Bitcoin - The largest cryptocurrency by market cap
    "ethereum",         # Ethereum - The second largest cryptocurrency
    "binancecoin",      # Binance Coin - Binance's native token
    "cardano",          # Cardano - Smart contract platform
    "solana",           # Solana - High-performance blockchain
    "dogecoin",         # Dogecoin - Popular meme cryptocurrency
]

def fetch_api_data(url, params, retry_delay=60):
    # Common function to fetch data from API with retry
    try:
        response = requests.get(url, params=params)
        if response.status_code == 429:  # Rate limit
            print("Rate limit hit, waiting 60 seconds...")
            time.sleep(retry_delay)
            response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return None

def update_price_data(coin):
    # Update price data for a cryptocurrency
    try:
        print(f"\nProcessing {coin}...")
        
        # Get current price
        url = f"https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": coin,
            "vs_currencies": "usd"
        }
        
        data = fetch_api_data(url, params)
        if not data or coin not in data:
            print(f"Error: Could not find price data for {coin}")
            return False
            
        current_price = data[coin]["usd"]
        current_time = int(datetime.now().timestamp() * 1000)
        
        # Check if file exists and get last timestamp
        if os.path.exists(f"{coin}.csv"):
            with open(f"{coin}.csv", "r") as f:
                lines = f.readlines()
                if len(lines) > 1:
                    try:
                        last_timestamp = int(lines[-1].split(",")[0])
                        if current_time - last_timestamp < 86400000:
                            print(f"No new data for {coin}")
                            return True
                    except ValueError:
                        # If timestamp is in wrong format, we'll update the file
                        print(f"Invalid timestamp format in {coin}.csv, updating file...")
            mode = 'a'  # Append mode
        else:
            mode = 'w'  # Write mode (new file)
            print(f"Creating new data file for {coin}...")
        
        # Save price data
        with open(f"{coin}.csv", mode) as f:
            if mode == 'w':
                f.write("timestamp,price\n")
            f.write(f"{current_time},{current_price}\n")
        
        print(f"Successfully {'appended' if mode == 'a' else 'saved'} price for {coin}: ${current_price:,.2f}")
        return True
        
    except Exception as e:
        print(f"Error updating data for {coin}: {e}")
        return False

def print_trade(buy_price, sell_price):
    profit = sell_price - buy_price
    print(f"buying at:       {buy_price:>10.2f}")
    print(f"selling at:      {sell_price:>10.2f}")
    print(f"trade profit:    {profit:>10.2f}")

def mean_reversion(prices, n=5):
    total_profit = 0
    first_buy = None
    buy_price = None
    trades = []  # Store trade records
    
    for i in range(n, len(prices)):
        price = prices[i]
        mean = np.mean(prices[i-n:i])
        
        if price < mean * 0.98:  # Buy signal
            if buy_price is None:
                if first_buy is None:
                    first_buy = price
                buy_price = price
                trades.append({"type": "buy", "price": price})
                print(f"buying at:       {price:>10.2f}")
        elif price > mean * 1.02:  # Sell signal
            if buy_price is not None:
                profit = price - buy_price
                total_profit += profit
                trades.append({"type": "sell", "price": price, "profit": profit})
                print(f"selling at:      {price:>10.2f}")
                print(f"trade profit:    {profit:>10.2f}")
                buy_price = None
    
    if buy_price is not None:
        trades.append({"type": "buy", "price": buy_price})
        print(f"buying at:       {buy_price:>10.2f}")
    
    print("-" * 23)
    print(f"Total profit:    {total_profit:>10.2f}")
    if first_buy:
        print(f"First buy:       {first_buy:>10.2f}")
        print(f"Percent return:  {(total_profit/first_buy*100):>10.2f}")
    print()
    
    return total_profit, first_buy, trades

def simple_moving_average(prices, n=5):
    total_profit = 0
    first_buy = None
    buy_price = None
    trades = []  # Store trade records
    
    for i in range(n, len(prices)):
        price = prices[i]
        mean = np.mean(prices[i-n:i])
        
        if price > mean:  # Buy signal
            if buy_price is None:
                if first_buy is None:
                    first_buy = price
                buy_price = price
                trades.append({"type": "buy", "price": price})
                print(f"buying at:       {price:>10.2f}")
        else:  # Sell signal
            if buy_price is not None:
                profit = price - buy_price
                total_profit += profit
                trades.append({"type": "sell", "price": price, "profit": profit})
                print(f"selling at:      {price:>10.2f}")
                print(f"trade profit:    {profit:>10.2f}")
                buy_price = None
    
    if buy_price is not None:
        trades.append({"type": "buy", "price": buy_price})
        print(f"buying at:       {buy_price:>10.2f}")
    
    print("-" * 23)
    print(f"Total profit:    {total_profit:>10.2f}")
    if first_buy:
        print(f"First buy:       {first_buy:>10.2f}")
        print(f"Percent return:  {(total_profit/first_buy*100):>10.2f}")
    print()
    
    return total_profit, first_buy, trades

def run_strategies(coin):
    try:
        # Read price data from CSV file
        prices = []
        with open(f"{coin}.csv", "r") as f:
            next(f)  # Skip header line
            for line in f:
                try:
                    timestamp, price = line.strip().split(",")
                    prices.append(float(price))
                except ValueError:
                    continue
        
        # Check if we have enough data points
        if len(prices) < 10:
            print(f"Not enough price data for {coin} to run strategies")
            return None
        
        print(f"\nRunning strategies for {coin.upper()}...")
        
        # Run Simple Moving Average strategy
        print("\nSimple Moving Average Strategy Output:")
        sma_profit, sma_first_buy, sma_trades = simple_moving_average(prices)
        
        # Run Mean Reversion strategy
        print("\nMean Reversion Strategy Output:")
        mr_profit, mr_first_buy, mr_trades = mean_reversion(prices)
        
        # Calculate returns for both strategies
        sma_returns = (sma_profit / sma_first_buy * 100) if sma_first_buy else 0
        mr_returns = (mr_profit / mr_first_buy * 100) if mr_first_buy else 0
        
        # Format output for JSON file
        return {
            f"{coin}_prices": prices,
            f"{coin}_sma_profit": round(sma_profit, 2),
            f"{coin}_sma_returns": round(sma_returns, 2),
            f"{coin}_sma_trades": sma_trades,
            f"{coin}_mr_profit": round(mr_profit, 2),
            f"{coin}_mr_returns": round(mr_returns, 2),
            f"{coin}_mr_trades": mr_trades
        }
        
    except Exception as e:
        print(f"Error running strategies for {coin}: {e}")
        return None

# Main execution
if __name__ == "__main__":
    try:
        print("Starting cryptocurrency trading simulation...")
        
        results = {}
        
        # Update price data and run strategies for each coin
        for coin in coins:
            try:
                if update_price_data(coin):
                    # Run trading strategies
                    coin_results = run_strategies(coin)
                    if coin_results:
                        results[coin] = coin_results
                
            except Exception as e:
                print(f"Error processing {coin}: {str(e)}")
        
        # Save results
        if results:
            with open("results.json", "w") as f:
                json.dump(results, f, indent=4)
            print("\nResults saved successfully!")
        else:
            print("\nNo results to save!")
        
        print("\nDone!")
        
    except Exception as e:
        print(f"Critical error in main execution: {str(e)}")