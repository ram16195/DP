class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print(nums)
        d = {}
        
        for i in range(0,len(nums)):
            d[nums[i]] = i
            
        for i in range(0,len(nums)):
            complement = target - nums[i]
            print(complement)
            
            if complement in d and i!=d[complement]:
                return i,d[complement]
        
        
