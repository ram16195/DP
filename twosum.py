class Solution:
    def twoSum(self, nums, target):
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}   #hash table
        if len(nums) < 1:
            return 0
        
        for i in range(0,len(nums)):
            complement = target - nums[i]  #get complement
            if complement in hm:  # if complement in hash return the sum
                #print(hm)
                return(hm[complement],i)
            hm[nums[i]] = i  #else add the number
                
