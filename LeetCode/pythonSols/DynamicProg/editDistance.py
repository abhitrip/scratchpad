class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lenword1 = len(word1)
        lenword2 = len(word2)
        dp = [[0]*(lenword2+1) for i in range(lenword1+1)]
        for i in range(lenword1+1):
            for j in range(lenword2+1):
                if i==0:
                    dp[i][j] = j
                elif j==0:
                    dp[i][j] = i
                elif word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))+1
        return dp[lenword1][lenword2]
