class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        # A = [1,2,5,-7,2,6]
        startPos = 0
        endPos = 0
        currSum = 0
        maxSum = 0
        pos = [-1,-2]
        for i in range(len(A)):
            if(A[i]<0):
                startPos = i+1
                currSum = 0
                continue
            currSum += A[i]
            if currSum > maxSum:
                endPos = i
                pos = [startPos,endPos]
                maxSum = currSum
            elif currSum ==maxSum:
                endPos = i
                currLen = endPos - startPos +1
                prevLen = pos[1]-pos[0]+1
                if currLen>prevLen:
                    pos = [startPos,endPos]



        if len(pos)>0:
            arr = A[pos[0]:pos[1]+1]
            return arr
        else :
            return []

if __name__ =="__main__":
    sol = Solution()
    testArr = [0,0,-1973594324,-2038664370,-184803526,-1424268980 ]
    subArr = sol.maxset(testArr)
    for i in subArr:
        print i
