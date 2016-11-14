public class Solution {
    public int singleNumber(int[] nums) {

      int res=0;

      int[] num = new int[32];

      for(int num_i:nums)
      {
          for(int b=0;b<32;b++)
          {
              if((num_i&(1<<b))!=0)
                num[b]++;

          }



      }

     for(int i=0;i<32;i++)
     {
         int b=num[i]%3;
         if(b!=0)
            res+= (1<<i);
     }

     return res;

    }
}
