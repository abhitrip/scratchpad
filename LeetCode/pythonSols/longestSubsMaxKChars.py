import collections
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        indexMap = collections.defaultdict()
        start,maxLen = 0,0
        for idx,char in enumerate(s):
            indexMap[char] = idx
            if len(indexMap)>k:
                start = idx
                for ch in indexMap:
                    start = min(start,indexMap[ch])
                del indexMap[s[start]]
                start+=1

            maxLen = max(maxLen,idx-start+1)
        return maxLen
