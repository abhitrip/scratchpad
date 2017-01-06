class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        maxProdtillNow,minaProdtillNow=nums[0],nums[0]
        maxRes = maxProdtillNow
        for i in range(1,len(nums)):
            prevMax,prevMin = maxProdtillNow,minProdtillNow
            maxProdtillNow = max(nums[i],max(prevMin*nums[i],prevMax*nums[i]))
            minProdtillNow = min(nums[i],min(prevMax*nums[i],prevMin*nums[i]))
            maxRes = max(maxRes,maxProdtillNow)
        return maxRes    
            
        