class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        if len(nums)<2:
            return nums[0]
        n = len(nums)
        print n
        dp = [0 for i in range(n+1)]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            #print dp[i]
        return dp[n-1]



