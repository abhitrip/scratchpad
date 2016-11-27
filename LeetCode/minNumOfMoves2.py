class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = nums[len(nums)/2]
        moves = 0
        for item in nums:
            moves+= abs(item-mid)

        return moves
