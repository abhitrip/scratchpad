class Solution(object):

    def findMedianUtil(self,nums1,nums2,k):
        """
        This will get the Kth largest element on combiining nums1 and nums2
        """
        if len(nums1)>len(nums2):
            return self.findMedianUtil(nums2,nums1,k)
        if not nums1 and not nums2:
            return None
        if not nums1:
            return nums2[k-1]
        if k==1:
            return min(nums1[0],nums2[0])
        num1Idx = min(k/2,len(nums1))
        num2Idx = k-num1Idx
        midnum1 = nums1[num1Idx-1]
        midnum2 = nums2[num2Idx-1]
        if midnum1<midnum2:
            return self.findMedianUtil(nums1[num1Idx:],nums2,k-num1Idx)
        return self.findMedianUtil(nums1,nums2[num2Idx:],k-num2Idx) #(k - (k-num1Idx))

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1)+len(nums2)
        if l%2==0:
            return (self.findMedianUtil(nums1,nums2,l/2)+self.findMedianUtil(nums1,nums2,l/2+1))/2.0
        return self.findMedianUtil(nums1,nums2,l/2+1)



class Solution(object):
    def getKth(self,a,astart,b,bstart,k):
        if len(a)<=astart:
            return b[bstart+k-1]
        elif len(b)<=bstart:
            return a[astart+k-1]
        elif k==1:
            return min(a[astart],b[bstart])

        midA,midB= 1<<31,1<<31
        if astart+k/2-1<len(a):
            midA=a[astart+k/2-1]
        if bstart+k/2-1<len(b):
            midB=b[bstart+k/2-1]
        if midA<midB:
            return self.getKth(a,astart+k/2,b,bstart,k-k/2)
        return self.getKth(a,astart,b,bstart+k/2,k-k/2)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m,n = len(nums1),len(nums2)
        return (self.getKth(nums1,0,nums2,0,(m+n+1)/2)+self.getKth(nums1,0,nums2,0,(m+n+2)/2))/2.0




