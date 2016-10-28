class Solution(object):

    def explore(self,v):
        print self.graph[v]
        if len(self.graph[v])==0:
            self.visited[v] = True
            return
        self.visited[v] = True
        for u in self.graph[v]:
            if self.visited[u]==False:
                self.explore(u)
                self.visited[u] = True




    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.graph = {}
        # Constructing graph
        for i in range(n):
            self.graph[i] = []
        print "graph = " , self.graph
        for edge in edges:
            u = edge[0]
            v = edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)


        comp = 0


        self.visited = [False for v in range(n)]
        for u in range(n):
            if self.visited[u]==False:
                comp+=1
                self.explore(u)
                print self.visited

        return comp


if __name__=="__main__":
    n = 2
    edges = [[1,0]]
    sol = Solution()
    connectedComp = sol.countComponents(n,edges)
    print "Number of connectedComp = %d " %connectedComp
