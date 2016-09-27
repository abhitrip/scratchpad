class Solution:
    # @param A : integer
    # @return a strings=

    def countAndSayHelper(self, A):
        strA = str(A)
        dig0 = strA[0]
        i = 0
        currDig = dig0
        currCnt = 0
        res = ""
        while i<len(strA):
            #print currDig
            j=i
            while strA[j]==currDig:
                currCnt+=1
                j+=1
                if j==len(strA):
                    break


            res += str(currCnt)+currDig

            if j!=i and j<len(strA):
                currDig = strA[j]
                currCnt = 0
                i=j
            else:
                i=j+1
                currCnt=0


        return res
    def countAndSay(self,A):
        n = 1
        num = 1
        while (n<A):
            str_i = self.countAndSayHelper(num)
            num = int(str_i)
            print num
            n+=1
        return str(num)




if __name__=="__main__":
    sol = Solution()
    res = sol.countAndSay(4)
    print res


