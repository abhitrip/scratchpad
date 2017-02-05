
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int size = nums.size();
        unordered_map<int,int> map;
        
        for(int i=0;i<size;i++)
        {
            int req = target-nums[i];
            if(map.count(req)>0)
            {
                int idx = map[req];
                vector<int> res{idx,i};
                return res;
            }
            map[nums[i]] = i;
            
        }
        
        return vector<int> {-1,-1};
    }
};

