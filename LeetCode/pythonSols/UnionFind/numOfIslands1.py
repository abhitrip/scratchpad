class UnionFind(object):
    def __init__(self,m,n,grid):
        self.n = n
        self.size = [0]*(m*n)
        self.id = [None]*(m*n)
        self.count = 0
        self.m = m
        self.add(grid,m,n)

    def genIndex(self,i,j):
        return i*self.n+j

    def add(self,grid,i,j):
        rows,cols = self.m,self.n
        for i in range(rows):
            for j in range(cols):
                idx = self.genIndex(i,j)
                self.count+= 1 if grid[i][j]=='1' else 0
                self.id[idx] = idx
                self.size[idx] = 1

    def find(self,p):
        while self.id[p]!=p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self,p,q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot==qRoot:
            return
        small,big = (pRoot,qRoot) if self.size[pRoot]<self.size[qRoot] else (qRoot,pRoot)
        self.id[small] = self.id[big]
        self.size[big]+=self.size[small]
        self.count-=1


class Solution(object):

    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def mergeIslands(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1':
                grid[i][j]='0'
                map(mergeIslands,(i+1,i-1,i,i),(j,j,j+1,j-1))
                return 1
            return 0

        return sum(mergeIslands(i,j) for i in range(len(grid)) for j in range(len(grid[0])))

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0 or len(grid[0])==0 : return 0
        m,n = len(grid),len(grid[0])
        uf = UnionFind(m,n,grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='0':
                    continue
                idx = uf.genIndex(i,j)
                if i>0 and grid[i-1][j]=='1':
                    uf.union(idx,idx-n)
                if i<m-1 and grid[i+1][j]=='1':
                    uf.union(idx,idx+n)
                if j>0 and grid[i][j-1]=='1':
                    uf.union(idx,idx-1)
                if j<n-1 and grid[i][j+1]=='1':
                    uf.union(idx,idx+1)

        return uf.count



