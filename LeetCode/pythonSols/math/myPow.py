class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0: return 1
        if n<0:
            x = 1/x
            n = abs(n)
        rem = 1 if n%2==0 else x
        return rem*self.myPow(x**2,n/2)