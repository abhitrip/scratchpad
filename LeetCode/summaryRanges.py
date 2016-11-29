class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i=0
        j=0
        res=[]
        while i<len(nums):
            j=i
            while j<len(nums)-1 and nums[j+1]-nums[j]==1:
                j+=1

            if j!=i:
                tmpStr = str(nums[i])+"->"+str(nums[j])
                res.append(tmpStr)
                i=j+1
            else:
                res.append(str(nums[i]))
                i+=1
        return res

