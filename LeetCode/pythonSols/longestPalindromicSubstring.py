class Solution(object):
    def helper(self,string,left,right):
        while left>=0 and right<len(string) and string[left]==string[right]:
            left-=1
            right+=1
        return string[left+1:right]


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        longestPal = ""
        lenLongestPal = 0
        for i in range(length):
            str1 = self.helper(s,i,i)
            if len(str1)>=lenLongestPal:
                longestPal = str1
                lenLongestPal = len(str1)

            str2 = self.helper(s,i,i+1)
            if len(str2)>=lenLongestPal:
                longestPal = str2
                lenLongestPal = len(str2)

        return longestPal





