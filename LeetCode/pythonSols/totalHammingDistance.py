class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total,N = 0,len(nums)
        for bit in range(32):
            bitset=0
            for num in nums:
                bitset+=1 if num &(1<<bit) else 0
            total += (N-bitset)*bitset
        return total

