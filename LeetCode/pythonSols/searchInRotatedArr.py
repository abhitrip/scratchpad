class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int7
        """
        l,r = 0,len(nums)-1
        while l<r:
            mid = (l+r)/2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid

        minIdx = l
        if target>=nums[minIdx] and target<=nums[-1]:
            beg,end = minIdx,len(nums)-1
        else:
            beg,end = 0,minIdx-1


        while beg<=end:
            mid = (beg+end)/2
            if nums[mid]>target:
                end = mid-1
            elif nums[mid]<target:
                beg = mid+1
            else:
                return mid

        return beg if nums[beg]==target else -1


