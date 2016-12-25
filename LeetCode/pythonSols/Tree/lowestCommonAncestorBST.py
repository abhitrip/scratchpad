# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None or p==None or q==None:
            return None
        maxpq = max(p.val,q.val)
        minpq = min(p.val,q.val)

        if root.val>=minpq and root.val<=maxpq:
            return root

        if root.val>=maxpq and root.val>=minpq:
            return self.lowestCommonAncestor(root.left,p,q)

        return self.lowestCommonAncestor(root.right,p,q)


