class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # Simple BFS Approach
        inf = (1<<31)-1
        if not rooms:
            return

        m,n = len(rooms),len(rooms[0])
        queue = collections.deque((i,j) for i in range(m) for j in range(n) if rooms[i][j]==0)
        def updateDist(i,j,ref):
            if 0<=i<m and 0<=j<n and rooms[i][j]==inf:
                rooms[i][j]=ref+1
                queue.append((i,j))
        while queue:
            gate = queue.popleft()
            """
            disp = ((1,0),(-1,0),(0,1),(0,-1))
            for d in disp:
                nx,ny = gate[0]+d[0],gate[1]+d[1]
                if 0<=nx<=m-1 and 0<=ny<=n-1 and rooms[nx][ny]==inf:
                    rooms[nx][ny]=rooms[gate[0]][gate[1]]+1
                    queue.append((nx,ny))
            """
            x,y = gate[0],gate[1]
            ref = rooms[x][y]
            map(updateDist,(x+1,x-1,x,x),(y,y,y-1,y+1),(ref,ref,ref,ref))

