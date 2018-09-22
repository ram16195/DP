class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(2,len(cost)):
            cost[i]=min(cost[i-1],cost[i-2])+cost[i]
        print(cost)
        return min(cost[-1],cost[-2])   
    
    '''
    for each value in cost from 2 . i put in the min of 2 precious + current cosr
    simple on
    
    
    '''
        
