class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        satisfied = 0
        sidx = 0
        gidx = 0
        while gidx < len(g) and sidx<len(s):
            greed = g[gidx]
            if s[sidx]>=greed:
                satisfied+=1
                gidx+=1
            sidx+=1


        return satisfied
