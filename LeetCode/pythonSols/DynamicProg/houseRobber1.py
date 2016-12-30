class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        robCurr,notRobCurr,total=0,0,0
        for bounty in nums:
            total = max(robCurr+bounty,notRobCurr)
            notRobCurr,robCurr = total,notRobCurr

        return total


