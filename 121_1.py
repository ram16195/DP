'''
Best time to buy stock, default == largest gap in array
'''

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        print(max_profit)
