class Solution:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        n = len(a) # Number of rows and number of columns
        diagList = [[] for i in range(2*n-1)]
        x = 0
        for i in range(n):
            startx = i
            starty = 0
            currx = startx
            curry = starty
            while(currx>=0) and (curry<n):
                diagList[x].insert(0,a[currx][curry])
                currx-=1
                curry+=1
            x+=1

        for i in range(1,n):
            startx = n-1
            starty = i
            currx = startx
            curry = starty
            while(currx>=0) and(curry<n):
                diagList[x].insert(0,a[currx][curry])
                currx-=1
                curry+=1
            x+=1

        return diagList


if __name__ == "__main__":
    x = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    antiDiag = sol.diagonal(x)
    for lst in antiDiag:
        for item in lst:
            print item,
        print
