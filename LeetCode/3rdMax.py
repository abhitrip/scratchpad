class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            a = Set(sorted(nums))
            if len(a)<3:
                return list(a)[-1]
        maxSet = set()
        i = 0
        while i<len(nums) and len(maxSet)!=3:
            maxSet.add(nums[i])
            i+=1
        print maxSet
        if i==len(nums):
            if len(maxSet)<3:
                return list(maxSet)[-1]
            else:
                return list(maxSet)[0]
        maxSet = list(set(maxSet))
        maxSet.sort()
        maxSet = list(set(maxSet))
        while i<len(nums):
            if nums[i] not in maxSet:
                if maxSet[0]>nums[i]:
                    i+=1
                    continue
                elif maxSet[2]<nums[i]:
                    maxSet.pop(0)
                    maxSet.append(nums[i])
                elif nums[i]>maxSet[0]:
                    maxSet.pop(0)
                    maxSet.append(nums[i])
                    maxSet.sort()
            i+=1
        return maxSet[0]


if __name__=="__main__":
    sol = Solution()
    a = [5,2,4,1,3,6,0]
    print "3rdmax = ",sol.thirdMax(a)
