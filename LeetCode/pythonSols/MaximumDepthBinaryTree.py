# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        
        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)
        return max(lDepth,rDepth)+1