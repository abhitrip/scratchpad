class UnionFind(object):
    """docstring for UnionFind"""
    def __init__(self):
        self.id = {}
        self.size = {}
        self.count = 0

    def add(self,p):
        self.id[p]  = p
        self.size[p] = 1
        self.count +=1


    def find(self,p):
        while p!=self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def unite(self,p,q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot==qRoot:
            return
        big,small = (pRoot,qRoot) if self.size[pRoot]>self.size[qRoot] else (qRoot,pRoot)
        self.id[small] = self.id[big]
        self.size[big]+=self.size[small]
        self.count-=1


class Solution(object):
    """docstring for Solution"""
    def numIslands2(self,m,n,positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        """
        Based on top Leetcode solution
        """

        ans = []
        islands = UnionFind()
        for pos in map(tuple,positions):
            islands.add(pos)
            displacement = ((-1,0),(1,0),(0,1),(0,-1))
            for dis in displacement:
                neighbor = (pos[0]+dis[0],pos[1]+dis[1])
                if neighbor in islands.id:
                    islands.unite(pos,neighbor)

            ans.append(islands.count)


        return ans


if __name__=="__main__":
    m,n=3,3
    positions=[[0,0],[0,1],[1,2],[2,1]]
    sol = Solution()
    ans = sol.numIslands2(m,n,positions)
    for isle in ans:
        print isle

