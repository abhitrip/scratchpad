# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = []
        while root!=None:
            self.stk.append(root)
            root = root.left


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stk)!=0


    def next(self):
        """
        :rtype: int
        """
        node = self.stk.pop()
        if node.right!=None:
            self.stk.append(node.right)
            left = node.right.left
            while left!=None:
                self.stk.append(left)
                left = left.left

        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
