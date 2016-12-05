class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations)<1:
            return 0
        citations.sort()
        length = len(citations)

        hidx = 0
        for idx,cits in enumerate(citations):
            if length-idx>=cits:
                hidx = cits
        return hidx
