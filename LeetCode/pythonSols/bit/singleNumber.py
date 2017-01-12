class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def xor(a,b):
            return a^b
        
        return reduce(xor,nums)
        