public class Solution {
    public void setZeroes(int[][] matrix) {
      int i=0;int j=0;
      boolean setRow=false;
      boolean setCol = false;
      for(;i<matrix.length;i++)
      {
          if(matrix[i][0]==0)
                setCol=true;
      }
      for(i=0;i<matrix[0].length;i++)
        if(matrix[0][i]==0)
            setRow = true;

      for( i=1;i<matrix.length;i++)
      {
          for( j=1;j<matrix[0].length;j++)
          {
              if(matrix[i][j]==0)
              {
                  matrix[0][j] = 0;
                  matrix[i][0] = 0;
              }
          }
      }

      for(i=1;i<matrix.length;i++)
      {
          if(matrix[i][0]==0){
          for( j=1;j<matrix[i].length;j++)
            matrix[i][j]=0;

          }
      }

      for( i=1;i<matrix[0].length;i++)
      {
          if(matrix[0][i]==0){
          for( j=1;j<matrix.length;j++)
            matrix[j][i]=0;

          }
      }

      if(setRow)
      {
          for( i=0;i<matrix[0].length;i++)
            matrix[0][i]=0;

      }

      if(setCol)
      {
          for( i=0;i<matrix.length;i++)
            matrix[i][0]=0;

      }






    }
}
