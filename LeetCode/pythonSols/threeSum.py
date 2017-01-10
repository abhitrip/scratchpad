class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums)<3:
            return []
        l = len(nums)
        i,j,k,res = 0,0,l-1,[]
        while i<l-2:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j,k = i+1,l-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    res.append([nums[i],nums[j],nums[k]])
                    while j<l-1 and nums[j]==nums[j+1]: j+=1
                    while k>0 and nums[k]==nums[k-1]: k-=1
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1


            i+=1
        return res

