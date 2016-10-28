class Solution(object):
    def backtrack(self,arr,x,n,cnt):
        if x>=n:
            return
        for i in range(cnt,n):
            x = x ^ (1<<i)
            print '{0:b}'.format(x)
            arr.append(x)
            self.backtrack(arr,x,n,cnt+1)
            x = x ^ (1<<i)




    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        x = 0
        st = 0
        arr=[]
        arr.append(x)
        self.backtrack(arr,x,n,st)
        return arr


if __name__ == "__main__":
    sol = Solution()
    res = sol.grayCode(3)
    print res
