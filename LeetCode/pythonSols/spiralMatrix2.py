class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n<1:
            return []
        if n==1:
            return [[1]]

        left,right,top,bot=0,n-1,0,n-1
        res=[[0]*n for i in range(n)]
        x = 1
        while left<=right and top<=bot:
            # First populate Top Row
            j=left
            while j<=right:
                res[top][j]=x
                x+=1
                j+=1
            top+=1

            # Then Populate right col
            i = top
            while i<=bot:
                res[i][right]= x
                x+=1
                i+=1
            right-=1


            # populate Bot row if not already populated
            j = right
            while j>=left and top<=bot:
                res[bot][j]=x
                x+=1
                j-=1
            bot-=1


            # populate left col if not already populated
            i = bot
            while i>=top and left<=right:
                res[i][left]=x
                x+=1
                i-=1
            left+=1

        return res




