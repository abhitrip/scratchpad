class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        numPoints = len(X)
        totalDispacement = 0
        for i in range(1,numPoints):
            prevX = X[i-1]
            currX = X[i]

            prevY = Y[i-1]
            currY = Y[i]

            xDisplacement = abs(currX-prevX)
            yDisplacement = abs(currY-prevY)


            displacement = max(xDisplacement,yDisplacement)
            totalDispacement+=displacement

        return totalDispacement


if __name__=="__main__":
    X = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
    Y = [ 4, -15, -10, -3, -13, 12, 8, -8 ]
    sol = Solution()
    print "The total number of steps = %d" %sol.coverPoints(X,Y)

