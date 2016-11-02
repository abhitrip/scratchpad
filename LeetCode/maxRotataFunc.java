public class Solution {
    public int maxRotateFunction(int[] A) {
        int wsum=0,sum=0;
        for(int i=0;i<A.length;i++)
            {
                wsum+=i*A[i];
                sum+=A[i];
            }
        int maxSum = wsum;
        int currSum = wsum;
        for(int i=1;i<A.length;i++)
        {
            currSum = currSum+sum-A.length*A[A.length-i];
            maxSum = Math.max(maxSum,currSum);
        }
        return maxSum;
    }
}
