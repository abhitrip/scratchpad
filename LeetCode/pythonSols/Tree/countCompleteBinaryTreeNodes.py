# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left,right = root,root
        ht = 0
        while right!=None:
            right = right.right
            left = left.left
            ht+=1
        if left==None:
            return (1<<ht)-1

        return self.countNodes(root.left)+self.countNodes(root.right)+1

