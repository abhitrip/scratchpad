class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return x

        r = min(x,(1<<16))
        l = 1
        while l<r:
            mid = (l+r)/2
            if mid*mid>x:
                r=mid
            elif mid*mid<x:
                l = mid
            elif mid*mid==x:
                return mid

            if (l==r-1):
                break

        return l



