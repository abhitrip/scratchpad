public class merge2SortedArrays {

    public static int[] merge(int[] a,int[]b)
    {
        int[] res = new int[a.length+b.length];
        int i=0;int j=0,k=0;
        while(i<a.length && j<b.length)
        {
            if(a[i]<b[j])
            {
                res[k] = a[i];
                i++;
            }
            else
            {
                res[k] = b[j];
                j++;
            }
            k++;
        }
        while(i<a.length)
        {
            res[k] = a[i];
            k++;
            i++;
        }
        while(j<b.length)
        {
            res[k] = b[j];
            k++;
            j++;
        }
        return res;
    }
    public static void main(String[] args) {
        int[] arr1 = new int[]{1,8,10,11};
        int[] arr2 = new int[]{2,7,20,30};
        int[] res = merge(arr1,arr2);
        for(int x:res)
            System.out.println(x);
    }
}
