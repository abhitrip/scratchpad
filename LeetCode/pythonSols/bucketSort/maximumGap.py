class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2: return 0
        minInt = -(1<<31)
        maxInt = (1<<31)-1
        maxNum,minNum = minInt,maxInt

        for num in nums:
            maxNum = max(maxNum,num)
            minNum = min(minNum,num)

        l = len(nums)
        intervalSize = (maxNum-minNum)/float(l-1)

        numBuckets = (maxNum-minNum)/intervalSize
        maxBuckets = [minInt]*l
        minBuckets = [maxInt]*l
        for num in nums:
            bucketIdx = min((num-minNum)/l,numBuckets-1)
            #print bucketIdx
            maxBuckets[bucketIdx] = max(maxBuckets[bucketIdx],num)
            minBuckets[bucketIdx] = min(minBuckets[bucketIdx],num)
        prev,gap = maxBuckets[0],0

        print maxBuckets,minBuckets
        for i in range(1,numBuckets):
            if minBuckets[i]==maxInt:
                continue
            gap = max(gap,minBuckets[i]-prev)
            prev = maxBuckets[i]

        return gap







