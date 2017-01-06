class Solution(object):
    def isMatch(self,s,p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        plength = len(p)
        slength = len(s)
        dp = [[False]* (plength+1) for i in range(slength+1)]
        dp[0][0] = True
        for i in range(1,plength+1):
            dp[0][i] = dp[0][i-2] if i>1 and p[i-1]=='*' else dp[0][i]

        for i in range(1,slength+1):
            for j in range(1,plength+1):
                if s[i-1]==p[j-1] or p[j-1]=='.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j] = dp[i][j-2] if j>1 else dp[i][j]
                    if p[j-2]=='.' or p[j-2]==s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                else:
                    dp[i][j] = False

        return dp[slength][plength]

if __name__=="__main__":
    sol = Solution()
    testcases = [("aa","a"),("aa","aa"),("aaa","aa"),("aa", "a*"),("aa", ".*"),("ab", ".*"),("aab", "c*a*b")]
    for s,p in testcases:
        print sol.isMatch(s,p)
