# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def dfs(self,root):

        self.stk.append(str(root.val))
        if root.left==None and root.right==None:
            tmpSum = ''.join(self.stk)
            self.leafsum+= int(tmpSum)
            print self.stk
            self.stk.pop()
            return

        if root.right!=None:
            self.dfs(root.right)

        if root.left!=None:
            self.dfs(root.left)

        self.stk.pop()

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        self.leafsum = 0
        self.stk = []
        self.dfs(root)
        return self.leafsum




