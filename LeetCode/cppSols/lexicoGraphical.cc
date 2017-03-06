#include <vector>
using namespace std;
class Solution {
public:
    void dfs(int curr, int n, vector<int> &res)
    {
        if(curr>n)
            return;
        res.push_back(curr);
        for(int i=0;i<10;i++)
        {  if(curr*10+i>n)
                return;
            dfs(curr*10+i,n,res);
        }   
        
    }
    vector<int> lexicalOrder(int n) {
        int i=1;
        vector<int> res;
        for(int i=1;i<10;i++)
            dfs(i,n,res);
        return res;
    }
};