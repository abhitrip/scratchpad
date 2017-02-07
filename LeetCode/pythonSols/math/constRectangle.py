class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        res = [area,1]
        start = int(math.sqrt(area))
        while start>0:
            if area%start==0 : 
                return [area/start start]
            start-=1
        return res
        
        