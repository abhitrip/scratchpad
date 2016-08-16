class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 0
        currSum = 1
        arrayLen = len(A)
        plusOneArr = []
        for i in range(arrayLen-1,-1,-1):
            currSum = currSum+A[i]+carry
            carry = currSum//10
            currSum = currSum%10
            plusOneArr.append(currSum)
            currSum = 0
        if carry >0:
            plusOneArr.append(carry)
        plusOneArr = plusOneArr[-1::-1]
        nonZeroStart = 0
        for i in range(len(plusOneArr)):
            if plusOneArr[i]!=0:
                nonZeroStart=i
                break


        return plusOneArr[nonZeroStart:]

if __name__=="__main__":
    A =  [2,5,6,8,6,1,2,4,5]
    sol = Solution()
    plusOneArr = sol.plusOne(A)
    for i in plusOneArr:
        print i,
