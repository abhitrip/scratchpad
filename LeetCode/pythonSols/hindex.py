class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations)<1:
            return 0
        buckets = [0 for i in range(len(citations)+1)]
        n = len(citations)
        for item in citations:
            if item>=n:
                buckets[n]+=1
            else:
                buckets[item]+=1

        count = 0
        for idx in range(n,-1,-1):
            count+=buckets[idx]
            if count>=idx:
                return idx

        return 0
