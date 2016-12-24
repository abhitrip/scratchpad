class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,j,maxLen=0,0,0
        charMap = [-1]*256 # Map of characters with positions
        for idx,ch in enumerate(s):
            ascii = ord(ch) # ascii val of character
            if charMap[ascii]!=-1: # if char has already occured then change i to maximum of previously occured characters
                i = max(i,charMap[ascii]+1)
            j+=1  # always increase destination index

            charMap[ascii] = idx
            maxLen = max(j-i,maxLen) # maxLen is j-i

        return maxLen

