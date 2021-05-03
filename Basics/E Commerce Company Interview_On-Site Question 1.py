def stock_profit(prices):

    if len(prices) < 2:
        raise Exception('Need more than 1 stock price.')

    min_price = prices[0]

    max_profit = prices[1] - prices[0]

    for price in prices[1:]:

        min_price = min(price, min_price)

        comparison_profit = price - min_price

        max_profit = max(comparison_profit, max_profit)

    return max_profit

prices = [12,11,15,3,10,33]
print(stock_profit(prices))