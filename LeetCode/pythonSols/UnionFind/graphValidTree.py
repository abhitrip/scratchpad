class UnionFind(object):
    """docstring for UnionFind"""
    def __init__(self, n):
        self.id = range(n)
        self.size = [1]*n
        self.count = n

    def find(self,p):
        while self.id[p]!=p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p



class Solution(object):
    """docstring for Solution"""


    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        uf = UnionFind(n)
        def union(edge):
            u,v = map(uf.find,edge)
            big,small = (u,v) if uf.size[u]>uf.size[v] else (v,u)
            uf.id[small] = big
            uf.size[big]+=uf.size[small]
            return u!=v

        return len(edges)==n-1 and all(map(union,edges))


