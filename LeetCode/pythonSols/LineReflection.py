class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        pointSet = set()
        xMax,xMin = -(1<<31),(1<<31)
        for point in points:
            pointSet.add(tuple(point))
            xMax = max(xMax,point[0])
            xMin = min(xMin,point[0])

        lineMul2 = (xMax+xMin)
        for point in points:
            if (lineMul2-point[0],point[1]) in pointSet:
                continue
            else:
                return False

        return True

