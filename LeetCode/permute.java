import java.util.*;
class permute  {

    public static void permute(int[]arr,List<List<Integer>> res,List<Integer> tmp,int start)
    {
        if(tmp.size()==arr.length)
        {
            res.add(new ArrayList<>(tmp));
            return;
        }

        for(int i=0;i<arr.length;i++)
        {
            if(tmp.contains(arr[i]))
                continue;
            tmp.add(arr[i]);
            permute(arr,res,tmp,0);
            tmp.remove(tmp.size()-1);
        }

    }
    public static void main(String[] args) {
        int x=0;
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        int[] arr = new int[]{1,2,3};
        permute(arr,res,tmp,0);
        for(List<Integer> l:res)
        {
            for(int m:l)
                System.out.print(m);
            System.out.println();
        }
    }
}
