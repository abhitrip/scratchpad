# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0
        if len(intervals)<2: return 1
        sortedIntervals = sorted(intervals,key = lambda x: x.start)
        heap = []
        firstItem = sortedIntervals[0].end,sortedIntervals[0].start
        heapq.heappush(heap,firstItem)
        for i in range(1,len(sortedIntervals)):
            popped = heapq.heappop(heap)
            interval = sortedIntervals[i]
            if interval.start<popped[0]: # i.e. interval's start<popped's end
                heapq.heappush(heap,(interval.end,interval.start))
            elif interval.start>=popped[0]:
                popped = (interval.end,popped[1])

            heapq.heappush(heap,popped)

        return len(heap)
