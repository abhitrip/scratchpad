class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m,n=len(matrix),len(matrix[0])
        sizes = [[0]*n for i in range(m)]
        res = 0
        for i in range(n):
            sizes[0][i]=ord(matrix[0][i])-ord('0')
            res = max(res,sizes[0][i])

        for i in range(m):
            sizes[i][0]=ord(matrix[i][0])-ord('0')
            res = max(res,sizes[i][0])

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=='1':
                    sizes[i][j] = min(min(sizes[i-1][j],sizes[i-1][j-1]),sizes[i][j-1])+1
                    res = max(res,sizes[i][j])


        return res*res




