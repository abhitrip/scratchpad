class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictMap = [-1]*256
        start,end=0,0
        maxSub,maxLen="",0
        for idx,char in enumerate(s):
            if dictMap[ord(char)]!=-1:
                start = max(start,dictMap[ord(char)]+1)
            dictMap[ord(char)]=idx
            maxLen = max(maxLen,idx-start+1)
        return maxLen

