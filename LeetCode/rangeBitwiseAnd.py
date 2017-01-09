class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Taken from top rated solution
        total,leftShiftAmt = 0,0
        while m!=n:
            m>>=1
            n>>=1
            leftShiftAmt+=1
        return (1<<leftShiftAmt)*m

