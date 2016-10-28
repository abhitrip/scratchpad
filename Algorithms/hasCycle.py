class Graph():
    """docstring for Graph"""
    def __init__(self, vertex):
        self.vertex = vertex
        self.adj = [[] for i in range(vertex)]
    def createGraph(self):
        self.adj[0].append(1)
        self.adj[0].append(2)
        self.adj[1].append(2)
        self.adj[2].append(0)
        self.adj[2].append(3)
        self.adj[3].append(3)
        print self.adj
    def explore(self,v):
        self.color[v] = 1
        for ver in self.adj[v]:
            if self.color[ver] == 1:
                return True
            if self.color[ver] ==0:
                flag = self.explore(ver)
                if flag==True:
                    return True
        self.color[v] = 2
        return False


    def isCycle(self):
        self.color = [0 for i in range(self.vertex)]
        for i in range(self.vertex):
            if self.color[i]==0:
                if self.explore(i):
                    return True
        return False



if __name__ == '__main__':
    obj = Graph(4)
    obj.createGraph()
    print obj.isCycle()










