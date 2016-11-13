public class Solution {
    public int findMin(int[] nums) {
        int l=0;int r= nums.length-1;
        int mid=0;
        int[] a = nums;
        while(l<=r-1)
        {
            if(r-l==1)
                return Math.min(a[l],a[r]);
            mid = l+(r-l)/2;
           if(a[mid]>a[r])
            l = mid;
          else
            r = mid;


        }

       if(a[l]>a[r])
        return a[r];
      return a[l];


    }
}
