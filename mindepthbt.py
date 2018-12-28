# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        queue = []
        level = 1

        queue.append((root,level))
        while queue:
            s,level = queue.pop(0)
            if s is None:
                return 0
            if s.left is None and s.right is None:
                return level
            level = level+1
            if s.left:
                queue.append((s.left,level))
            if s.right:
                queue.append((s.right,level))
                
