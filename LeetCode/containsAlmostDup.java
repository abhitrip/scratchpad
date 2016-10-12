import java.util.*;
class Pair{
    int val;
    int idx;
    public Pair(int v,int i){
        this.val = v;
        this.idx = i;
    }
}
public class containsAlmostDup  {
     public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if((nums.length==0)||(k<=0))
            return false;
        Set<Integer> treeset = new TreeSet<>();
        for(int i=0;i<nums.length;i++)
        {
            Integer floor = treeset.floor(nums[i]+t);
            Integer ceiling = treeset.ceiling(nums[i]-t);
            if((floor!=null)&&(Integer.valueOf(floor)>=nums[i]))
                return true;
            if((ceiling!=null)&&(Integer.valueOf(floor)<=nums[i]))
                return true;
            treeset.add(nums[i]);
            if(i>=k)
            {
                treeset.remove(nums[i-k]);
            }
        }
        return false;
    }
    public boolean containsNearbyAlmostDuplicate2(int[] nums,int k,int t){
        if((nums.length==0)||(k<=0))
            return false;
        Pair[] arr = new Pair[nums.length];
        Pair tmp= null;
        int i=0,j=0;
        for(int i=0;i<nums.length;i++)
        {
            tmp = new Pair(nums[i],i);
            arr[i] = tmp;
        }
        Arrays.sort(arr,new Comparator<Pair>(){
            @Override
            public int compare(Pair obj1,Pair obj2){
                return obj1.val -obj2.val;
            }
        });

        for(i=0;i<arr.length;i++)
        {   j=i+1;
            while(j<arr.length &&((Math.abs(pair[i].val-pair[j].val))<t))
            {
                int index = Math.abs(pair[j].idx-pair[i].idx);
                if(index<=k)
                    return true;
            }
        }
        return false;

    }

}
