# Given a array of numbers representing the stock prices of a company inchronological order, 
# write a function that calculates the maximumprofit you could have made from buying and selling that stock. 
# You're also given a number fee that represents a transaction fee for each buy
# This problem was asked by Affirm.
# You must buy before you can sell the stock, but you can make as manyand sell transaction.
# For example,given [1,3,2,8,4,10]and fee = 2,
# you should returntransactions as you like.
# since you could buy the stock at 1 dollar, and sell at 8 dollars
# and then buy it at 4 dollars and sell it at 10 dollars, 
# Since we didtwo transactions,there is a 4 dollar fee, 
# so we have 7+ 6 = 13 profit minus 4 dollars of fees.

def max_profit(prices, fee):
    # 初始化：第一天买入的成本
    hold = -prices[0]  # 持有股票的最大收益
    cash = 0  # 不持有股票的最大收益
    profit = 0  # 记录每天的总利润

    print(f"Day 0: Price = {prices[0]}, Hold = {hold}, Cash = {cash}, Profit = {profit}")

    # 遍历价格数组，从第二天开始
    for i in range(1, len(prices)):
        # 计算第 i 天持有股票的最大收益
        new_hold = max(hold, cash - prices[i])

        # 计算第 i 天不持有股票的最大收益
        new_cash = max(cash, hold + prices[i] - fee)

        # 更新变量
        hold, cash = new_hold, new_cash

        # 计算利润（因为最终利润是 `cash`，所以我们用它作为 daily profit）
        profit = cash

        # 打印每天的利润变化
        print(f"Day {i}: Price = {prices[i]}, Hold = {hold}, Cash = {cash}, Profit = {profit}")

    # 返回最后一天不持有股票的最大利润
    return cash

# 测试
prices = [3,1, 3, 2, 8, 4, 10]
fee = 2
profit = max_profit(prices, fee)
print(f"Final Maximum Profit: {profit}")
