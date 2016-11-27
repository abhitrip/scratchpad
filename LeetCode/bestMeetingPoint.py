class Solution(object):
    def minTotalDistance(self, grid):
        """ro
        """
        # The idea is to find median point in x axis then y axis of the points
        rows = []
        cols = []
        numRows = len(grid)
        numCols = len(grid[0])
        for rowid,row in enumerate(grid):
            for colid,element in enumerate(row):
                if element==1:
                    rows.append(rowid)
                    cols.append(colid)
        print rows

        medianY = (rows[(len(rows)-1)/2] + rows[len(rows)/2])/2
        cols.sort()
        print cols
        medianX = (cols[(len(cols)-1)/2] + cols[len(cols)/2])/2

        # Now compute the Manhattan distances
        print medianY,medianX
        distance = 0
        for r,row in enumerate(grid):
            for c,col in enumerate(row):
                if col==1:
                    distance += abs(r-medianY)+abs(c-medianX)

        return distance

