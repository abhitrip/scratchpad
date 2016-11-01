public class BinaryIndexTree {
    public static int getSum(int[] tree,int idx)
    {
        int sum=0;
        idx = idx+1;
        while(idx>0)
        {
            sum+=tree[idx];
            idx-=(idx&(-idx));
        }
        return sum;
    }
    public static void updateTree(int[] tree,int idx,int val)
    {
        int i = idx+1;
        while(i<tree.length)
        {
            tree[i]+=val;
            i+= (i&(-i));
        }
    }
    public static int[] constructTree(int[] inp)
    {
        int[] bitree = new int[inp.length+1];
        for(int i=0;i<inp.length;i++)
            updateTree(bitree,i,inp[i]);
        return bitree;
    }


    public static void main(String[] args) {
        int[] array = new int[]{2,1,1,3,2,3,4,5,6,7,8,9};
        int n = array.length;
        int[] BITree = constructTree(array);
        System.out.println(getSum(BITree,5));
    }
}
