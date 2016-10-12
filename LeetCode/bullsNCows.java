import java.util.*;
public class bullsNCows {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();

        int i=0,j=0;
        for(i=0;i<nums.length;i++)
        {

            Integer last = map.put(nums[i],i);
            if((last!=null)&&(Integer.valueOf(last)+k>=i))
            {
                return true;

            }


        }
        return false;
    }
    public static void main(String[] args)
    {
        int[] nums = new int[]{2,2};
        bullsNCows obj = new bullsNCows();
        boolean hasDup = obj.containsNearbyDuplicate(nums,3);
        System.out.println(hasDup);
    }

}
