class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        bucketmap = {}
        for idx,num in enumerate(nums):
            buckidx,offset = (num/t,1) if t!=0 else (num,0)
            for i in range(buckidx-offset,buckidx+offset+1):
                if i in bucketmap and abs(bucketmap[i]-num)<=t:
                    return True
            bucketmap[buckidx] = num
            if len(bucketmap)>k:
                del bucketmap[nums[idx-k]/t if t!=0 else nums[idx-k]]        
        return False

