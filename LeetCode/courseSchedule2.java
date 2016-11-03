public class Solution {

    Map<Integer,List<Integer>> graph;
    int[] color;
    final int WHITE = 0;
    final int GRAY = 1;

    public void topological(Map<Integer,List<Integer>> graph,Set<Integer>visited,int v,List<Integer>stk)
    {

        visited.add(v);

        List<Integer> adj = graph.get(v);

        for(int u:adj)
        {

            if(!visited.contains(u)){
                visited.add(u);
                topological(graph,visited,u,stk);
            }


        }

        stk.add(v);


    }

    public boolean hasCycle(Map<Integer,List<Integer>> graph,int[] color,int v)
    {

        color[v] = GRAY;
        List<Integer> adj = graph.get(v);
        for(int u:adj)
        {
            if(color[u]==GRAY)
                return true;
            if(color[u]==WHITE && hasCycle(graph,color,u))
                return true;
        }
        color[v] = 2;//black
        return false;

    }

    public int[] findOrder(int numCourses, int[][] prerequisites) {

        graph = new HashMap<>();
        Set<Integer>visited = new HashSet<>();
        List<Integer> stk = new ArrayList<>();
        int[] color = new int[numCourses];
        for(int i=0;i<numCourses;i++)
        {

            color[i]=0;
            graph.put(i,new ArrayList<>());
        }

        for(int i=0;i<prerequisites.length;i++)
        {
            int u = prerequisites[i][0];
            int v = prerequisites[i][1];

            List<Integer> edges = graph.get(v);
            edges.add(u);
            graph.put(v,edges);
        }

        for(int i : graph.keySet())
        {
            List<Integer> adj = graph.get(i);
            if(adj.size()<1)
                continue;
            for(int j:adj)
                System.out.println(i+" -> "+ j);
        }

        // First find if cycle exists or not
        boolean cycle=false;
        for(int v=0;v<numCourses;v++)
        {
            if(color[v]==WHITE)
                {
                    cycle = hasCycle(graph,color,v);
                    if(cycle)
                        return new int[]{};
                }

        }




        // First Do Topological Sort
        boolean flag = false;
        for(int v=0;v<numCourses;v++)
        {
            if(!visited.contains(v))
            {
               topological(graph,visited,v,stk);
            }
        }

        int[] res = new int[numCourses];
        for(int x=0;x<res.length;x++)
            res[x] = stk.get(numCourses-x-1);
        return res;

    }
}
