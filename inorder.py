# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        Steps:
        current -< root
        while current.left
        add to stack
        once null
        pop, print then
        try right and go back to adding, 
        \else done
        
        O(n) + O(n) space
        recursive O(n) + O(h) space, implicit stack
        
        
        '''
        if not root:
            return []
        current = root
        
        s = []
        p = []
        done = 0
        while not done:
            if current is not None:
                
                s.append(current)
                current = current.left
            else:
                if len(s) > 0:
                    current = s.pop()
                    p.append(current.val)
                    current = current.right
                else:
                    done = 1
        return p
        
        
        
        if not root:
            return []
        p = []
        self.inorderTraversal(root.left)
        print(root.val)
        self.inorderTraversal(root.right)
