class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        x = dict()
        repeated = 0
        l = len(A)
        for i in A:
            if i in x:
                repeated = i
                break
            x[i]=1

        sumOfList = sum(A)-repeated
        missingNum = (l*(l+1))//2 -sumOfList
        return [repeated,missingNum]
    def repeatedNumber2(self,A):
        """
        This is the better zero memory solution for the
        case
        sum of list = n(n+1)/2 -A + B
        sum of squares of list = n(n+1)(2n+1)/6 - A^2 + B^2
        """
        n = len(A)
        sumOfNums = (n*(n+1))//2
        sumOfSqrs = sumOfNums*(2*n+1)//3
        s = sum(A)
        sqrS = reduce(lambda x,y: x+y,map(lambda x: x**2,A))

        X = s- sumOfNums
        Y = sqrS - sumOfSqrs
        aPlusb = Y/X
        aMinusB = X
        a = (aPlusb + aMinusB)/2
        b = (aPlusb - aMinusB)/2
        return [a,b]




if __name__=="__main__":
    testArr = [3,1,2,5,3]
    testObj = Solution()
    result  = testObj.repeatedNumber2(testArr)
    print "The repeated number is %d and the missing number is %d" %(result[0],result[1])
