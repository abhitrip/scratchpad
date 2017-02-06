class Solution(object):
    """
    This is to find (a^b)%1337, where b is a number written
    in form of a list
    """
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        def powMod(x,y):
            """
            computes x^y%1337
            """
            res = 1
            for i in range(y):
                res = (res*x)%1337
            return res
            
        if not b:
            return 1 
        dig = b[-1]
        b.pop()
        return powMod(self.superPow(a,b),10)*powMod(a,dig)