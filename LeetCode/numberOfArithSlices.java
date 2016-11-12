
public class numberOfArithSlices {
    public int numberOfArithmeticSlices(int[] A)
    {
        int sum=0;
        //int[] dp = new int[A.length];
        if(A.length<3)
            return 0;

        for(int i=1;i<A.length;i++)
        {
            int currDiff = A[i]-A[i-1];
            for(int j=i+1;j<A.length;j++)
            {
                if(A[j]-A[j-1]==currDiff)
                    sum+=1;
                else
                    break;
            }


        }


        return sum;
    }
}
