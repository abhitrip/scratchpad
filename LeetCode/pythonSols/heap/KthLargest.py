import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for idx,num in nums:
            if idx<k:
                heapq.heappush(heap,num)
                continue
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap,num)

        return heap[0]

                
            
        