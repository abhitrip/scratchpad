class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = collections.defaultdict()

        for idx,num in enumerate(nums):
            if target-num in hashMap: return [hashMap.get(target-num),idx]
            hashMap[num] = idx

        return [0,0]


