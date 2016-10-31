import java.util.*;
import java.lang.*;

public class LargestNumber {
    public static String largestNumber(int[] nums){
        Integer[] numArr = new Integer[nums.length];
        for(int i=0;i<nums.length;i++)
            numArr[i] = nums[i];
        Arrays.sort(numArr,new Comparator<Integer>(){
            @Override
            public int compare(Integer i1,Integer i2)
            {
                String val1 = String.valueOf(i1)+String.valueOf(i2);
                String val2 = String.valueOf(i2)+String.valueOf(i1);
                return val1.compareTo(val2);
            }
        });
        StringBuilder sb = new StringBuilder();
        for(int i=nums.length-1;i>=0;i--)
            sb.append(String.valueOf(numArr[i]));
        String res =  sb.toString();
        int j=0;
        while(j<res.length()-1&&res.charAt(j)=='0')
            j++;

        return res.substring(j);
    }
    public static void main(String[] args) {
        int[] nums = {3,30,34,5,9};
        System.out.println(largestNumber(nums));
    }
}
