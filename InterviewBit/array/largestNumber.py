class Solution:
    # @param A : tuple of integers
    # @return a strings

    def largestNumber(self, A):
        listA = []
        for i in A:
            listA.append(i)
        """
        for i in  range(len(listA)):
            for j in range(i+1,len(listA)):
                num = str(listA[i])+str(listA[j])
                revNum = str(listA[j])+str(listA[i])
                if num<revNum :
                    listA[i], listA[j]= listA[j], listA[i]
        """
        def compare(x,y):
            return (int(str(x)+str(y)) - int(str(y)+str(x)))

        print "list A = ",listA
        listA = sorted(listA,reverse=True)
        print "list A = ",listA
        strA = ""
        for i in range(len(listA)):
            strA+=str(listA[i])

        if int(strA)==0:
            return "0"
        else:
            return strA


if __name__=="__main__":
    a = [1,2,3,10,5]
    sol = Solution()
    print sol.largestNumber(a)
