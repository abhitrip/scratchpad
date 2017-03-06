class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None 
    
class Solution(object):
    def isValidSerialization(self,preorder):
        """
        type preorder: str
        rtype : bool
        """
        stack = []
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack.append(root)
        for num in preorder

http://linkedin.com/in/abhitrip
http://github.com/abhitrip
http://abhitrip.github.io/