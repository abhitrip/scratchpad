class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char,pair<int,int>> myMap;
        for(int i=0;i<s.size();i++)
        {
            myMap[s[i]].first+=1;
            myMap[s[i]].second = i;
            
        }
        int minIdx = (1<<31)-1;
        for(auto &p: myMap)
        {
            if(p.second.first==1)
                minIdx = min(minIdx,p.second.second);
        }
        return minIdx==(1<<31)-1?-1:minIdx;
        

    }
    
};