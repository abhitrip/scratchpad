class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Solution 1
        """
        i,j=0,0
        while i<len(s) nad j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1

        return i==len(s)
        """
        # Solution 2
        itert = iter(t)
        res = all(c in itert for c in s)
        return res

