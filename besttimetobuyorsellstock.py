    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        '''
        buy = prices[0]
        res = 0
        for p in prices:
            print(p,buy,res)
            if buy > p: # current price is less than last buy
                buy = p # buy at p
            else:
                tmp = p - buy - fee
                if tmp > 0: # have profit
                    res += tmp
                    buy = p - fee 
        return res
        '''
        
        '''
        class Solution {
    public int maxProfit(int[] prices, int fee) {
        int[] hold = new int[prices.length + 1];
        int[] notHold = new int[prices.length + 1];
        hold[0] = Integer.MIN_VALUE;
        notHold[0] = 0;
        
        for (int i = 0; i < prices.length; i++) {
            hold[i + 1] = Math.max(hold[i], notHold[i] - prices[i] - fee);
            notHold[i + 1] = Math.max(notHold[i], hold[i] + prices[i]);
        }
        
        return notHold[prices.length];
    }
}
        '''
        hold = [None]*(len(prices)+1)
        nothold = [None]*(len(prices)+1)
        hold[0] = float('-Inf')
        nothold[0] = 0
        for i in range(0,len(prices)):
            hold[i+1] = max(hold[i],nothold[i]-prices[i]-fee)
            nothold[i+1] = max(nothold[0],hold[i]+prices[i])
        return(nothold[-1])
