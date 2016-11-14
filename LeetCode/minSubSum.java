public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
       int x=0;
       int minLen = Integer.MAX_VALUE;
       int start = 0;
       if(nums.length==0)
            return 0;
       int i=0;
       while(i<nums.length)
       {
           x+=nums[i];
           if(x>=s)
           {
              
               while(x>=s)
               {
                   
                   minLen = Math.min(minLen,i-start+1);
                   x=x-nums[start++];
                   
                   
               }                   
               
           }
           i++;
       }
       return minLen==Integer.MAX_VALUE?0:minLen;
    }
}