import java.util.*;
public class Solution {
    List<List<Integer>> adj;
    Set<Integer> visited;
    public boolean hasCycle(int u,int par)
    {
        visited.add(u);
        for(int v: adj.get(u))
        {
            if((visited.contains(v) && v!=par)||(!visited.contains(v) && hasCycle(v,u)))
                return true;
        }
        return false;
    }
    public boolean validTree(int n, int[][] edges) {
        visited = new HashSet<>();
        adj = new ArrayList<>();
        for(int i=0;i<n;i++)
            adj.add(new ArrayList<>());
        for (int[] edge:edges)
        {
            int u=edge[0],v=edge[1];
            adj.get(u).add(v);
            adj.get(v).add(u);
        }


        boolean cycle = hasCycle(0,-1);
        if(cycle)
            return false;

        for(int i=0;i<n;i++)
            if(!visited.contains(i))
                return false;
        return true;


    }
}
