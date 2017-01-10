class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # Adapted from 2 solutions from leetcode
        stk = []
        for d in num:
            while k and stk and stk[-1]>d:
                stk.pop()
                k-=1
            stk.append(d)

        while k:
            stk.pop()
            k-=1
        numRemoved=  ''.join(stk).lstrip('0') or '0'
        return numRemoved


