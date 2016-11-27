class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minVal = (1<<31)-1
        for item in nums:
            minVal = min(item,minVal)
        moves = 0
        for item in nums:
            moves+=(item-minVal)

        return moves

