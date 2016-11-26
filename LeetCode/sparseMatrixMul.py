class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        m,n,p = len(A),len(A[0]),len(B[0])
        sparseA = [[] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j]!=0:
                    sparseA[i].append((j,A[i][j]))

        AB = [ [0]*p for i in range(m)]

        for i in range(m):
            aSparse = sparseA[i]
            for idx,val in aSparse:

                for j in range(p):
                    AB[i][j]+= val*B[idx][j]


        return AB






