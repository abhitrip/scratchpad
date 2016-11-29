class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        sumPosMap = {}
        sumPosMap[0] = 0
        maxLen,cumsum=0,0
        for idx,num in enumerate(nums):
            cumsum+=num
            if cumsum-k in sumPosMap:
                maxLen = max( maxLen,idx-sumPosMap.get(cumsum-k)+1)
            if cumsum not in sumPosMap:
                sumPosMap[cumsum] = idx+1

        return maxLen





