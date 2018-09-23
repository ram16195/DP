class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current = float('inf')
        profit = 0
        ans = 0
        for i in prices:
            current = min(current,i)
            profit = i-current
            if profit > 0:
                ans = ans+profit
                current = i
                profit = 0
        return ans
            
        
