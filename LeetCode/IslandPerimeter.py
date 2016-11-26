class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                cnt = 0
                if i>0 :
                    cnt+= 1 if grid[i-1][j]==1 else 0
                if i<rows-1:
                    cnt+= 1 if grid[i+1][j]==1 else 0
                if j>0:
                    cnt+=1 if grid[i][j-1]==1 else 0
                if j<cols-1:
                    cnt+= 1 if grid[i][j+1]==1 else 0
                
                perimeter+= 4-cnt if grid[i][j]==1 else 0
        
        return perimeter