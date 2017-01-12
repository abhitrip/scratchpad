class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def xor(a,b):
            return a^b
        xorall = reduce(xor,nums)
        findLastSetBit = xorall &(-xorall) # Find last set bit = n&(-n)
        num1,num2=0,0
        for num in nums:
            if num&findLastSetBit!=0:
                num1^=num
            else:
                num2^=num
        return [num1,num2]