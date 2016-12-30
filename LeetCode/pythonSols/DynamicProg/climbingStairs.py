class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """


        if n<3:
            return n
        p = 2
        pp = 1
        for i in range(3,n+1):
            curr = p+pp
            p,pp = curr,p

        return curr
