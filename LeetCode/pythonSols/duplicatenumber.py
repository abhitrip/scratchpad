class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n<2: return -1
        slow,fast = nums[0],nums[nums[0]]
        while slow!=fast:
            slow,fast = nums[slow],nums[nums[fast]]
    
     
        slow = 0
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
    
        return slow
    
         
         