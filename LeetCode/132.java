public class Solution {
    public boolean find132pattern(int[] nums) {
        if(nums.length<3)
            return false;
        TreeSet<Integer> tset = new TreeSet<>();
        int[] minarr = new int[nums.length];
        minarr[0] = Integer.MAX_VALUE;
        int currMin = nums[0];
        // Min of all elements
        for(int i=1;i<nums.length;i++)
        {
            currMin = Math.min(currMin,nums[i-1]);
            minarr[i] = currMin;
            currMin = minarr[i];
            //System.out.println(currMin);
        }
        Integer floor=null,ceil=null;
        for(int i=nums.length-1;i>=1;i--)
        {

            if(minarr[i]>nums[i])
                continue;

            //floor = tset.floor(nums[i]);
            ceil = tset.ceiling(minarr[i]+1);
            if(ceil!=null && ceil<nums[i])
                {
                    System.out.println( minarr[i]+" " +nums[i] +" "+ceil  );
                    return  true;
                }

            tset.add(nums[i]);
        }

        return false;

    }
}
