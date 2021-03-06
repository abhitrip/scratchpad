# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return root

        left  = self.invertTree(root.left)
        right = self.invertTree(root.right)
        left,right = right,left
        root.right = right
        root.left = left
        return root

