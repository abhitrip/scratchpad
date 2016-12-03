class Solution(object):
    def findMedianUtil(self,A,B,n):
        if len(A)>len(B):
            return self.findMedianUtil(B,A,n)
        if len(A)==0 and len(B)==0:
            return None
        if len(A)==0:
            return B[n-1]
        if n==1:
            return min(A[0],B[0])

        k = n/2
        pa = min(len(A),k)
        pb = n-pa
        if A[pa-1]<B[pb-1]:
            # 1st n/2 elements in A , so look in A[n/2:] and B[0:]
            return self.findMedianUtil(A[pa:],B,n-pa)
        else:
            return self.findMedianUtil(A,B[pb:],n-pb)





    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totalLength = len(nums1)+len(nums2)
        if totalLength%2==1:
            return self.findMedianUtil(nums1,nums2,totalLength/2+1)
        else:
            return (self.findMedianUtil(nums1,nums2,totalLength/2)+self.findMedianUtil(nums1,nums2,totalLength/2+1))/2.0


