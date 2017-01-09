class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0] : return -1
        m,n,buildings = len(grid),len(grid[0]),sum(item for row in grid for item in grid if item==1)
        dist = [[0]*n for i in range(m)]
        minDist = -1
        def bfs(i,j,walk):
            minDist = -1
            bfsQ = collections.deque([(i,j,0)])
            while bfsQ:
                x,y,d = bfsQ.popleft()
                for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if 0<=nx<m and 0<=ny<n and gridCopy[nx][ny]==walk:
                        bfsQ.append((nx,ny,d+1))
                        dist[nx][ny]+=d+1
                        gridCopy[nx][ny]-=1
                        if minDist==-1 or minDist>dist[nx][ny]:
                            minDist = dist[nx][ny]
            return minDist

        walk = 0
        gridCopy = [[grid[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    minDist = bfs(i,j,walk)
                    walk-=1

        return minDist
