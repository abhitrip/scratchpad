# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        resMax,l = 0,len(points)
        for i in range(l):
            a,b = points[i].x,points[i].y
            plMap = collections.defaultdict()
            plMap['inf']=0
            same = 1
            for j in range(i+1,l):
                x,y = points[j].x,points[j].y
                mx = x-a
                my = y-b
                if x==a and y==b:
                    same+=1
                    continue
                if mx==0:
                    slope = 'inf'
                else:
                    slope = float(my)/mx
                if slope not in plMap:
                    plMap[slope]=0
                plMap[slope]+=1
            
            maxCollinear = max(plMap.values())
            resMax = max(resMax,maxCollinear+same)
        
        return resMax
                    
                    
                    
                    