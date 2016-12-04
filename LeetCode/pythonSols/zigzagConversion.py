class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        rowString = [[] for i in range(numRows)]

        idx = 0
        delta = 1
        for char in s:
            idx = max(0,idx)
            idx = min(idx,numRows-1)
            rowString[idx].append(char)
            if idx==numRows-1 and delta>0:
                delta=-delta
            elif idx==0 and delta<0:
                delta=-delta
            idx+=delta


        combinedRow = [''.join(x) for x in rowString]
        res = ""
        for row in combinedRow:
            res+=row

        return res
