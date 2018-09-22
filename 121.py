class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        
        '''
        DP explanation:  We need to find the max price we can sell something at, essentially similar to max subarray problem
        O(N) - go through all the prices
        minprice = min minprice, current price
        profit = price-minprice
        max = max profit,maxprofit
        
        simply remember the values over time
        
        
        
        '''
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        print(max_profit)
        
