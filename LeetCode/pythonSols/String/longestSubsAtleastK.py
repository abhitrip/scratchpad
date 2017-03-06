import collections
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        
        if len(s)<1: return 0
        dic = collections.Counter(s)
        mySet = set(i for i in dic.keys() if dic[i]<k)
        if len(mySet)==0: return len(s)
        start = 0
        intervals = []
        while start<len(s):
            if s[start] in mySet:
                start+=1
            else:
                i = start
                while start<len(s) and s[start] not in mySet:
                    start+=1
            
                intervals.append((i,start))
        maxSub = 0    
        for start,end in intervals:
            maxSub = max(self.longestSubstring(s[start:end],k),maxSub)
        return maxSub
        
        
        