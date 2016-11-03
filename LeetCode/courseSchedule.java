public class Solution {

    final int WHITE = 0;
    final int GRAY = 1;
    final int BLACK = 2;
    public boolean hasCycle(Map<Integer,List<Integer>> graph,int[]visited,int v)
    {
        visited[v] = 1;
        List<Integer> adj = graph.get(v);
        for(int u : adj)
        {
            if(visited[u]==1)
                return true;
            if(visited[u]==0 && hasCycle(graph,visited,u))
                return true;
        }
        visited[v] = 2;
        return false;


    }


    public boolean canFinish(int numCourses, int[][] prerequisites) {

        Map<Integer,List<Integer>> graph = new HashMap<>();
        int[] visited = new int[numCourses];

        for(int k=0;k<numCourses;k++)
            graph.put(k,new ArrayList<>());
        for(int i=0;i<prerequisites.length;i++)
        {
            int v = prerequisites[i][0];
            int u = prerequisites[i][1];


            List<Integer> e = graph.get(u);
            e.add(v);
            graph.put(u,e);


        }
        for(int i=0;i<numCourses;i++)
            visited[i]=WHITE;
        for(int v:graph.keySet()){
            if(visited[v]==WHITE){
            if(hasCycle(graph,visited,v))
                return false;
            }
        }
        return true;
    }
}
