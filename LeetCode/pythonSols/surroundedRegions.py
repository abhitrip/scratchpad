class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        """
        bfs solution taken from Stefan pochman's solution
        """
        if len(board)<1 or len(board[0])<1:
            return

        m,n = len(board),len(board[0])
        border = [ij for idx in range(max(m,n)) for ij in ((idx,0),(idx,n-1),(0,idx),(m-1,idx))]
        while border:
            i,j = border.pop()
            if 0<=i<=m-1 and 0<=j<=n-1 and board[i][j]=='O':
                board[i][j]='#'
                border+= [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='#':
                    board[i][j] ='O'



