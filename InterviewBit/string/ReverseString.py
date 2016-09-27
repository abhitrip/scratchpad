class Solution:
    # @param A : string
    # @ retutn string
    def reverseWords(self,A):
        reverseStr=""
        currWord=""
        i = 0
        while i<len(A):
            while i<len(A) and A[i]!=' ':
                currWord+=A[i]
                i+=1
            if reverseStr=='':
                reverseStr = currWord
            else:
                reverseStr = currWord + " "+reverseStr
            while i<len(A) and A[i]==' ':
                i+=1
            if i==len(A):
                break
            currWord=""

        return reverseStr

if __name__=="__main__":
    sol = Solution()
    rev = sol.reverseWords("the sky is blue")
    print rev

