class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]: return 0
        heap = []
        m,n = len(heightMap),len(heightMap[0])
        visited = [[False]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    heapq.heappush(heap,(heightMap[i][j],i,j))
                    visited[i][j]=True

        res=0
        while heap:
            height,i,j = heapq.heappop(heap)
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<m and 0<=y<n and not visited[x][y]:
                    res += max(0,height-heightMap[x][y])
                    heapq.heappush(heap,(max(height,heightMap[x][y]),x,y))
                    visited[x][y]=True
        return res
