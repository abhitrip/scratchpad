class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stk = []
        currMin = -(1<<31)
        for num in preorder:
            if num<currMin:
                return False
            while stk and num>stk[-1]:
                currMin = stk.pop()
            stk.append(num)

        return True
