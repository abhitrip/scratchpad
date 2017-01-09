class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Taken from diet Pepsi's solution
        if n==1: return [0]
        adjList = [set() for i in range(n)]
        for u,v in edges:
            adjList[u].add(v)
            adjList[v].add(u)


        leaves = [i for i in range(n) if len(adjList[i])==1]

        while n>2:
            newLeaves = []
            for u in leaves:
                v = adjList[u].pop()
                adjList[v].remove(u)
                if len(adjList[v])==1: newLeaves.append(v)

            n-= len(leaves)
            leaves = newLeaves

        return leaves



