class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = nums
        current = maxsum = A[0]
        for i in A[1:]:
            current = max(i,current+i)   # check if current val is greater than sum of all prev, if not add i to current
            maxsum = max(maxsum,current) # check if the current maxsum is greater than current value, take max of maxsum, if neg wont increase
        return maxsum
        
