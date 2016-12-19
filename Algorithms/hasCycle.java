import java.util.*;
public class hasCycle {

    Map<Integer,List<Integer>> graph;
    int[] color;
    public hasCycle(int numVer)
    {
        graph = new HashMap<>();
        color = new int[numVer];
        for(int i=0;i<numVer;i++)
            color[i] = 0; // 0 == White, 1==Gray , 2==Black
        for(int i=0;i<numVer;i++)
            graph.put(i,new ArrayList<>());
    }

    public void addEdges(int u,int v)
    {
        List<Integer> adj = graph.get(u);
        adj.add(v);
        graph.put(u,adj);
    }

    public boolean cycle(int v)
    {
        color[v] = 1;
        List<Integer> adj = graph.get(v);
        for(int u : adj)
        {
            if(color[u]==1)
                return true;
            if(color[u]==0 && cycle(u))
                return true;
        }
        color[v] = 2;
        return false;
    }
    public static void main(String[] args) {
            hasCycle gph =   new hasCycle(4);
            gph.addEdges(0,1);
            gph.addEdges(0,2);
            //gph.addEdges(1,2);
            //gph.addEdges(2,0);
            // gph.addEdges(2,3);
            // gph.addEdges(3,3);
            for(int v = 0;v<4;v++)
            {
                if(gph.color[v]==0)
                {
                    if(gph.cycle(v))
                        {
                            System.out.println("Cycle");
                            return;
                        }
                }
            }
            System.out.println("noCycle");
        }
}
