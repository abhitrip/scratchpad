import  collections
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen,start = 0,0
        indexMap = collections.defaultdict()
        for idx,char in enumerate(s):
            indexMap[char] = idx
            if len(indexMap)>2:
                start = idx
                for ch in indexMap:
                    start = min(indexMap[ch],start)
                del indexMap[s[start]]
                start+=1

            maxLen = max(maxLen,idx-start+1)


        return maxLen

