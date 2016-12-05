class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0

        if len(nums)==1:
            return nums[0]

        curr1,pre1,tmp1=0,0,0
        curr2,pre2,tmp2=0,0,0

        for i in range(0,len(nums)-1):
            tmp1 = max(pre1+nums[i],curr1)
            pre1,curr1 = curr1,tmp1

        curr2,pre2,tmp2=0,0,0
        for i in range(1,len(nums)):
            tmp2 = max(pre2+nums[i],curr2)
            pre2,curr2 = curr2,tmp2

        return max(curr1,curr2)

