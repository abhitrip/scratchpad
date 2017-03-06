#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
class Solution{
    public : 
        vector<int> twoSum(vector<int> &nums,int target)
        {
            int i=0;
            unordered_map<int,int> map;
            for(;i<nums.size();i++)
            {
                if(map.count(target-nums[i]))
                    return vector<int>{map[target-nums[i]],i};
                map[nums[i]]=i;
            }
            return {0,0};
        }
};