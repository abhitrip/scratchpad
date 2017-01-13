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
            asciival =ord(char)
            if dictMap[asciival]!=-1:
                start = dictMap[asciival]+1
                if idx-start>=maxLen:

                    maxLen = max(maxLen,idx-start+1)
                    maxSub = s[start:idx]

            dictMap[asciival]= idx
        return maxLen

