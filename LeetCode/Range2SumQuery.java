public class Range2SumQuery {
    int [][] matrix ;
    int [][] dp;
    public Range2SumQuery(){
        matrix = new int[][]{
            {3, 0, 1, 4, 2},
            {5, 6, 3, 2, 1},
            {1, 2, 0, 1, 5},
            {4, 1, 0, 1, 7},
            {1, 0, 3, 0, 5}};
    }
    public void printMatrix()
    {
        int rows = matrix.length;
        int cols = matrix[0].length;
        for(int i=0;i<rows;i++)
        {
            for(int j=0;j<cols;j++)
                System.out.print(matrix[i][j]+",");
            System.out.println();
        }
    }
    public void numMatrix()
    {
        int rows = matrix.length;
        int cols = matrix[0].length;
        dp = new int[rows][cols];
        dp[0][0] = matrix[0][0];
        for(int i=1;i<cols;i++)
        {
            dp[0][i] = dp[0][i-1]+matrix[0][i];
        }
        for(int i=1;i<rows;i++)
        {
            dp[i][0] = dp[i-1][0] + matrix[i][0];
            for(int j=1;j<cols;j++)
            {
                dp[i][j] = dp[i][j-1] + dp[i-1][j]-dp[i-1][j-1]+matrix[i][j];
            }
        }

    }

    public void printDp()
    {
        numMatrix();
        int rows = matrix.length;
        int cols = matrix[0].length;
        for(int i=0;i<rows;i++)
        {
            for(int j=0;j<cols;j++)
                System.out.print(dp[i][j]+",");
            System.out.println();
        }
    }
    public int SumRegion(int row1,int col1,int row2,int col2)
    {
        return dp[row2][col2]-dp[row1-1][col2]-dp[row2][col1-1]+dp[row1-1][col1-1];
    }

    public static  void main(String[] args){
        Range2SumQuery obj = new Range2SumQuery();
        obj.printMatrix();
        obj.printDp();
        System.out.println("****************Here's The Result of Queries*****************");
        System.out.println(obj.SumRegion(2,1,4,3));
        System.out.println(obj.SumRegion(1,1,2,2));
        System.out.println(obj.SumRegion(1,2,2,4));


    }

}
