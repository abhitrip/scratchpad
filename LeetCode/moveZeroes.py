class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numzeros = 0
        i = 0
        j = 0
        while i<len(nums) and j<len(nums):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            else:
                j+=1
        
         
        
        
        
        
        