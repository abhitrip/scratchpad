class Solution:
    # @param A : string
    # @return a list of integers
    def numOfOnes(seq):
        n = 0
        for i in seq:
            if i=='1':
                n+=1
        return n


    def flip(self, A):
        """
        Based on a slight modification of Kadane or maximum subarray problem
        """
        arr = [-1 if x =='1' else 1 for x in A]
        print arr
        bestSumNow = 0
        bestSum = 0
        pos = [-1,-1]
        l = 0
        r = 0
        for i in range(len(arr)):
            bestSumNow += arr[i]
            if bestSumNow<0:
                bestSumNow = 0
                l = i+1
            if bestSumNow > bestSum:
                r = i
                pos[0] = l
                pos[1] = r
                bestSum = bestSumNow
        if pos[0]==-1 :
            return [0,0]
        pos = [pos[0]+1,pos[1]+1]
        return pos

if __name__ == '__main__':
    sol = Solution()
    arr = "010"
    lr = sol.flip(arr)
    print lr[0],lr[1]
