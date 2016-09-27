# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval

    def doesOverlap(self,interval1,interval2):
        start1 = interval1.start
        start2 = interval2.start
        end1   = interval1.start
        end2   = interval2.start
        if ((start1-start2)*(end1-end2))<0:
            return True
        else:
            return False

    def mergeInterval(self,interval1,interval2):
        start = min(interval1.start,interval2.start)
        end   = max(interval1.end,interval2.end)
        return (start,end)

    def insert(self, intervals, new_interval):
        resultInterval = []
        toMerge = new_interval
        for interval in intervals:
            if self.doesOverlap(interval,toMerge)==True:
                merged = self.mergeInterval(interval,toMerge)
                resultInterval.append(merged)
                toMerge = merged
            else:
                resultInterval.append(interval)
        return resultInterval

if __name__=="__main__":
    int1 = Interval(1,3)
    int2 = Interval(6,9)
    merg = Interval(2,5)
    sol = Solution()
    res = sol.insert([int1,int2],merg)

    for item in res:
        print item



