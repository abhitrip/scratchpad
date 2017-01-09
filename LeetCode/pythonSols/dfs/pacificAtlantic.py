class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        m,n = len(matrix),len(matrix[0])
        pVisited = [[False for i in range(n)] for j in range(m)]
        aVisited = [[False for i in range(n)] for j in range(m)]


        def dfs(visited,i,j):
            # when dfs called, meaning its caller already verified this point
            visited[i][j] = True
            for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                x, y = i + d[0], j + d[1]
                if 0<=x<m and 0<=y<n and (not visited[x][y]) and matrix[x][y]>=matrix[i][j]:
                    dfs(visited,x,y)





        for i in range(m):
            dfs(pVisited,i,0)
            dfs(aVisited,i,n-1)

        for j in range(n):
            dfs(pVisited,0,j)
            dfs(aVisited,m-1,j)


        res = [[i,j] for i in range(m) for j in range(n) if pVisited[i][j] and aVisited[i][j]]
        return res




