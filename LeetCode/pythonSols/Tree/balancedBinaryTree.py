# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """


        def height(node):
            if node==None:
                return 0
            rheight = height(node.right)
            lheight = height(node.left)
            if rheight==-1 or lheight==-1 or abs(lheight-rheight)>1:
                return -1
            return max(lheight,rheight)+1


        if height(root)!=-1:
            return True


        return False



