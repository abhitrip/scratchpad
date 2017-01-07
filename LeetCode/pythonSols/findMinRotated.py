class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        if len(nums)<1:
            return 0
        elif len(nums)==1:
            return nums[0]

        """
        left,right = 0,len(nums)-1
        while left<right-1:
            mid = (left+right)/2

            if nums[mid]>nums[left] and nums[mid]>nums[right]:
                left = mid+1
            elif nums[mid]<nums[left] and nums[mid]<nums[right]:
                right = mid
            else:
                break
            print left,mid,right

        return min(nums[left],nums[right])
        """
        # More Efficient solution
        left,right = 0,len(nums)-1
        while left<right:
            mid = (left+right)/2

            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]


if __name__=="__main__":
    sol = Solution()
    arr = [5,6,7,0,1,2,4]
    print sol.findMin(arr)
