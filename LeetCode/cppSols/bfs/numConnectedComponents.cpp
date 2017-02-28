class Solution {
public:
    int countComponents(int n, vector<pair<int, int>>& edges) {
        if (!n) return 0;
        
        vector<int> adj[n];
        int u,v;
        // Make the adj List first
        for(auto &p: edges)
        {
            u = p.first;
            v = p.second;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        
        int conn=0;
        vector<bool> visited(n,false);
        for(int i=0;i<n;i++)
        {
            if (visited[i]) continue;
            conn++;
            visited[i] = true;
            queue<int> q;
            
            q.push(i);
            while(!q.empty())
            {
                u = q.front(); q.pop();
                for(int x: adj[u])
                {
                    if(!visited[x]){
                      q.push(x);
                      visited[x] = true;
                      
                    } 
                }
                
                
                
            }
            
        }
        return conn;
        
    }
};