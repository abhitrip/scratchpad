package LeetCodeHard;

/**
 * Created by abhitrip on 12/19/16.
 */
public class MedianOfSortedArrays {

    public int getKthElement(int[] a,int sa,int[] b,int sb,int k)
    {


        if(sa>=a.length)
            return b[sb+k-1];
        if(sb>=b.length)
            return a[sa+k-1];
        if(k==1)
            return Math.min(a[sa],b[sb]);
        int aMid = Integer.MAX_VALUE;
        int bMid = Integer.MAX_VALUE;
        if(a.length>sa+k/2-1)
            aMid = a[sa+k/2-1];
        if(b.length>sb+k/2-1)
            bMid = b[sb+k/2-1];
        if(aMid<bMid)
            return getKthElement(a,sa+k/2,b,sb,k-k/2);
        else
            return getKthElement(a,sa,b,sb+k/2,k-k/2);
    }

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int totLength = (nums1.length+nums2.length);
        double median = 0.0;
        if(totLength%2==1)
            median= Double.valueOf(getKthElement(nums1,0,nums2,0,totLength/2+1));
        else
            median = (getKthElement(nums1,0,nums2,0,totLength/2+1)+getKthElement(nums1,0,nums2,0,totLength/2))/2.0;
        return median;
    }
}
