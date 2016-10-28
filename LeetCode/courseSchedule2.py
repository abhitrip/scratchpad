class CourseSchedule(object):
    """docstring for CourseSchedule"""
    def __init__(self):
        self.stk = []

    def explore(self,v):
        print v
        self.color[v] = 1
        for i in self.adj[v]:
            if self.color[i]==0:
                self.explore(i)
        self.color[v] = 2
        self.stk.append(v)


    def topological(self,v):
        x = len(self.adj)
        self.color = [0 for i in range(x)]
        self.explore(v)


    def findOrder(self,numCourses,prerequisites):
        self.adj = [[] for i in range(numCourses)]
        for lst in prerequisites:
            self.adj[lst[0]].append(lst[1])

        v = 0
        maxV = 0
        for vertex in range(len(self.adj)):
            if len(self.adj[vertex])>maxV:
                v = vertex
                maxV = len(self.adj[vertex])

        print "v = ",v
        self.topological(v)


if __name__ == '__main__':
    obj = CourseSchedule()
    numCourses = 2
    prereqs =  [[1,0]]
    obj.findOrder(numCourses,prereqs)
    print obj.stk
