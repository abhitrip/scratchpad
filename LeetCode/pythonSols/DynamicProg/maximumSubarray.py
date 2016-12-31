class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        maxCurr,maxSoFar = nums[0],nums[0]
        for i in range(1,len(nums)):
            maxCurr = max(nums[i],maxCurr+nums[i])
            maxSoFar = max(maxCurr,maxSoFar)
        return maxSoFar
