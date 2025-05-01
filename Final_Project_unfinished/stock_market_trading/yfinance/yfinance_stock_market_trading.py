# Import required libraries
import json
import requests
import time
import numpy as np
from datetime import datetime, timedelta
import os
import yfinance as yf

# Define stocks to analyze with sector information
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

def fetch_stock_data(symbol):
    """
    Fetch one year of historical stock data using yfinance
    Args:
        symbol (str): Stock ticker symbol
    Returns:
        list: List of closing prices
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    stock = yf.Ticker(symbol)
    df = stock.history(start=start_date, end=end_date)
    return df['Close'].tolist()

def save_price_data(symbol, prices):
    """
    Save price data to CSV file
    Args:
        symbol (str): Stock ticker symbol
        prices (list): List of closing prices
    """
    csv_path = os.path.join(os.getcwd(), f"{symbol}.csv")
    with open(csv_path, "w") as f:
        f.write("Date,Price\n")
        for price in prices:
            f.write(f"{datetime.now().strftime('%Y-%m-%d')},{price}\n")

def print_trade(buy_price, sell_price):
    """
    Print trade information
    Args:
        buy_price (float): Buy price
        sell_price (float): Sell price
    """
    profit = sell_price - buy_price
    print(f"Buy price:       {buy_price:>10.2f}")
    print(f"Sell price:      {sell_price:>10.2f}")
    print(f"Trade profit:    {profit:>10.2f}")

def simple_moving_average(prices, n=5):
    """
    Simple Moving Average trading strategy
    Buy when price is above moving average, sell when below
    Args:
        prices (list): List of closing prices
        n (int): Number of days for moving average
    Returns:
        tuple: (total_profit, first_buy_price, trades)
    """
    total_profit = 0
    first_buy = None
    buy_price = None
    trades = []
    
    for i in range(n, len(prices)):
        price = prices[i]
        mean = np.mean(prices[i-n:i])
        
        if price > mean:  # Buy signal
            if buy_price is None:
                if first_buy is None:
                    first_buy = price
                buy_price = price
                trades.append({"type": "buy", "price": price})
                print(f"Buy signal at:   {price:>10.2f}")
        else:  # Sell signal
            if buy_price is not None:
                profit = price - buy_price
                total_profit += profit
                trades.append({"type": "sell", "price": price, "profit": profit})
                print(f"Sell signal at:  {price:>10.2f}")
                print(f"Trade profit:    {profit:>10.2f}")
                buy_price = None
    
    return total_profit, first_buy, trades

def mean_reversion(prices, n=5):
    """
    Mean Reversion trading strategy
    Buy when price is 2% below mean, sell when 2% above
    Args:
        prices (list): List of closing prices
        n (int): Number of days for mean calculation
    Returns:
        tuple: (total_profit, first_buy_price, trades)
    """
    total_profit = 0
    first_buy = None
    buy_price = None
    trades = []
    
    for i in range(n, len(prices)):
        price = prices[i]
        mean = np.mean(prices[i-n:i])
        
        if price < mean * 0.98:  # Buy signal
            if buy_price is None:
                if first_buy is None:
                    first_buy = price
                buy_price = price
                trades.append({"type": "buy", "price": price})
                print(f"Buy signal at:   {price:>10.2f}")
        elif price > mean * 1.02:  # Sell signal
            if buy_price is not None:
                profit = price - buy_price
                total_profit += profit
                trades.append({"type": "sell", "price": price, "profit": profit})
                print(f"Sell signal at:  {price:>10.2f}")
                print(f"Trade profit:    {profit:>10.2f}")
                buy_price = None
    
    return total_profit, first_buy, trades

def bollinger_bands(prices, n=5):
    """
    Bollinger Bands trading strategy
    Buy when price is 5% below mean, sell when 5% above
    Args:
        prices (list): List of closing prices
        n (int): Number of days for mean calculation
    Returns:
        tuple: (total_profit, first_buy_price, trades)
    """
    total_profit = 0
    first_buy = None
    buy_price = None
    trades = []
    
    for i in range(n, len(prices)):
        price = prices[i]
        mean = np.mean(prices[i-n:i])
        
        if price < mean * 0.95:  # Buy signal
            if buy_price is None:
                if first_buy is None:
                    first_buy = price
                buy_price = price
                trades.append({"type": "buy", "price": price})
                print(f"Buy signal at:   {price:>10.2f}")
        elif price > mean * 1.05:  # Sell signal
            if buy_price is not None:
                profit = price - buy_price
                total_profit += profit
                trades.append({"type": "sell", "price": price, "profit": profit})
                print(f"Sell signal at:  {price:>10.2f}")
                print(f"Trade profit:    {profit:>10.2f}")
                buy_price = None
    
    return total_profit, first_buy, trades

def check_last_day_signal(prices, strategy_name):
    """
    Check trading signal for the last day
    Args:
        prices (list): List of closing prices
        strategy_name (str): Name of the strategy
    Returns:
        str: "buy", "sell", or None
    """
    last_price = prices[-1]
    mean = np.mean(prices[-5:])
    
    if strategy_name == "Simple Moving Average":
        return "buy" if last_price > mean else "sell"
    elif strategy_name == "Mean Reversion":
        if last_price < mean * 0.98:
            return "buy"
        elif last_price > mean * 1.02:
            return "sell"
    elif strategy_name == "Bollinger Bands":
        if last_price < mean * 0.95:
            return "buy"
        elif last_price > mean * 1.05:
            return "sell"
    return None

def run_strategies(symbol):
    """
    Run all trading strategies for a given stock
    Args:
        symbol (str): Stock ticker symbol
    Returns:
        dict: Results for all strategies
    """
    # Fetch and save price data
    prices = fetch_stock_data(symbol)
    if not prices or len(prices) < 10:
        print(f"Not enough data for {symbol}")
        return None
    
    save_price_data(symbol, prices)
    
    print(f"\nAnalyzing {symbol}...")
    results = {}
    
    # Run Simple Moving Average strategy
    print("\nSimple Moving Average Strategy:")
    sma_profit, sma_first_buy, sma_trades = simple_moving_average(prices)
    sma_signal = check_last_day_signal(prices, "Simple Moving Average")
    results["Simple Moving Average"] = {
        "profit": sma_profit,
        "first_buy": sma_first_buy,
        "trades": sma_trades,
        "signal": sma_signal
    }
    
    # Run Mean Reversion strategy
    print("\nMean Reversion Strategy:")
    mr_profit, mr_first_buy, mr_trades = mean_reversion(prices)
    mr_signal = check_last_day_signal(prices, "Mean Reversion")
    results["Mean Reversion"] = {
        "profit": mr_profit,
        "first_buy": mr_first_buy,
        "trades": mr_trades,
        "signal": mr_signal
    }
    
    # Run Bollinger Bands strategy
    print("\nBollinger Bands Strategy:")
    bb_profit, bb_first_buy, bb_trades = bollinger_bands(prices)
    bb_signal = check_last_day_signal(prices, "Bollinger Bands")
    results["Bollinger Bands"] = {
        "profit": bb_profit,
        "first_buy": bb_first_buy,
        "trades": bb_trades,
        "signal": bb_signal
    }
    
    return results

def main():
    """
    Main function to run the trading analysis
    """
    all_results = {}
    best_stock = None
    best_strategy = None
    best_profit = float('-inf')
    
    for symbol in stocks:
        results = run_strategies(symbol)
        if results:
            all_results[symbol] = results
            
            # Find best performing strategy for this stock
            for strategy_name, strategy_results in results.items():
                if strategy_results["profit"] > best_profit:
                    best_profit = strategy_results["profit"]
                    best_stock = symbol
                    best_strategy = strategy_name
    
    # Save results to JSON file
    with open("results.json", "w") as f:
        json.dump({
            "all_results": all_results,
            "best_stock": best_stock,
            "best_strategy": best_strategy,
            "best_profit": best_profit
        }, f, indent=4)
    
    print("\nAnalysis complete!")
    print(f"Best performing stock: {best_stock}")
    print(f"Best strategy: {best_strategy}")
    print(f"Total profit: ${best_profit:.2f}")

if __name__ == "__main__":
    main()