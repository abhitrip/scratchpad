# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals: return True
        intervals.sort(key = lambda y:y.start)
        prev = intervals[0]
        for i in range(1,len(intervals)):
            if prev.end>intervals[i].start:
                return False
            prev = intervals[i]
        return True


