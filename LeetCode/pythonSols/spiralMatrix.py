class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)<1:
            return []
        
        res = [] #
        bot = len(matrix)-1
        right = len(matrix[0])-1
        left = 0
        top = 0
        while left<=right and top<=bot:
            j=left
            # Copying Top Row
            while j<=right:
                res.append(matrix[top][j])
                j+=1
            top+=1
            i = top
            while i<=bot:
                res.append(matrix[i][right])
                i+=1
            right-=1
            
            j=right
            while j>=left and top<=bot:
                res.append(matrix[bot][j])
                j-=1
            bot-=1
            
            i = bot
            while i>=top and left<=right:
                res.append(matrix[i][left])
                i-=1
            left+=1
        
        return res
            
        
            
        