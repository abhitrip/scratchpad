public class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean row[][] = new boolean[9][9];
        boolean col[][] = new boolean[9][9];
        boolean box[][] = new boolean[9][9];
        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                if(board[i][j]!='.')
                {

                    int dig = board[i][j]-'0';
                    if(row[i][dig-1])
                        return false;
                    else
                        row[i][dig-1] = true;


                    if(col[j][dig-1])
                        return false;
                    else
                        col[j][dig-1] = true;

                    if(box[3*(i/3)+j/3][dig-1])
                        return false;
                    else
                        box[3*(i/3)+j/3][dig-1]=true;


                }


            }
        }
        return true;
    }
}
