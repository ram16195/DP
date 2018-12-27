# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

    
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        current = root
        st = []
        done = 0
        res = []
        while(not done):
            if current is not None:
                st.append(current)
                current = current.left
            
            else:
                if(len(st)>0):
                    current = st.pop()
                    res.append(current.val)
                    current = current.right
                else:
                    done = 1
        print(res)
        #Twosum
        
        d = {}
        nums = res
        target = k
        
        for i in range(0,len(nums)):
            d[nums[i]] = i
            
        for i in range(0,len(nums)):
            complement = target - nums[i]
            print(complement)
            
            if complement in d and i!=d[complement]:
                return True
        
            
        
        
                
        
        

