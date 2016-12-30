class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        pow2map = collections.defaultdict()
        for i in range(32):
            pow2map[(1<<i)] = 1

        dp = [0]*(num+1)
        dp[0]



        pow2closest=0
        for i in range(1,num+1):
            if i in pow2map:
                dp[i] = pow2map[i]
                pow2closest = i
            else:
                dp[i] = dp[pow2closest]+dp[i-pow2closest]

        return dp
