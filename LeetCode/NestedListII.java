/**

 * // This is the interface that allows for creating nested lists.

 * // You should not implement it, or speculate about its implementation

 * public interface NestedInteger {

 *     // Constructor initializes an empty nested list.

 *     public NestedInteger();

 *

 *     // Constructor initializes a single integer.

 *     public NestedInteger(int value);

 *

 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.

 *     public boolean isInteger();

 *

 *     // @return the single integer that this NestedInteger holds, if it holds a single integer

 *     // Return null if this NestedInteger holds a nested list

 *     public Integer getInteger();

 *

 *     // Set this NestedInteger to hold a single integer.

 *     public void setInteger(int value);

 *

 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.

 *     public void add(NestedInteger ni);

 *

 *     // @return the nested list that this NestedInteger holds, if it holds a nested list

 *     // Return null if this NestedInteger holds a single integer

 *     public List<NestedInteger> getList();

 * }

 */

public class Solution {

    

    public void dfs(NestedInteger curr,List<List<Integer>> arr,int lev)

    {

        while(arr.size()<=lev)

            arr.add(new ArrayList<>());    

            

        System.out.println("arrsize= "+arr.size() + "lev="+ lev);

        if(curr.isInteger())

        {

            arr.get(lev).add(curr.getInteger());

                

            

        }

        List<NestedInteger> lst = curr.getList();

        for(int i=0;i<lst.size();i++)

        {

            dfs(lst.get(i),arr,lev+1);

        }

        

    }

    

    public int depthSumInverse(List<NestedInteger> nestedList) {

        int i = 0;

        int level=0;

        List<List<Integer>> levels = new ArrayList<>();

        for( i=0;i<nestedList.size();i++)

        {

            NestedInteger curr = nestedList.get(i);

            dfs(curr,levels,level);

        }

        

        int totLev = levels.size(),sum=0;

        for(i=0;i<totLev;i++)

        {

            for(int j=0;j<levels.get(i).size();j++)

                {

                    sum = sum+ (levels.get(i).get(j))*(totLev-i);

                    System.out.print(levels.get(i).get(j));

                }

            System.out.println();

        }

        

        return sum;

        

    }

}
