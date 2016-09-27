class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        i = 0
        lenOfStr = len(A)
        lCurrWord = 0
        lPrevWord = 0
        i = lenOfStr-1
        while i>=0 and A[i]==' ':
            i-=1
        while i>=0 and A[i]!=' ' :
            lCurrWord+=1
            i-=1
        return lCurrWord

if __name__=="__main__":
    sol = Solution()
    length = sol.lengthOfLastWord("Hello World ")
    print length
