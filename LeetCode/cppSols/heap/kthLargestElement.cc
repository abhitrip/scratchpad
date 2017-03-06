#include <iostream>
#include <queue>
#include <vector>


class Solution{
    public:
        int findKthLargest(std::vector<int>& nums, int k) {
           auto comp = [](int x, int y){ return x > y; };
            std::priority_queue<int,std::vector<int>,decltype(comp)> heap(comp);
            for(int i=0;i<nums.size();i++)
            {
                if(heap.size()<k)
                    heap.push(nums[i]);
                else
                {
                    if(heap.top()<nums[i])
                        {
                            heap.pop();
                            heap.push(nums[i]);
                        }

                }
            }


            return heap.top();
            
    }
};

int main()
{
    std::vector<int> x = {3,2,1,5,6,4};
    Solution s;
    std::cout<<s.findKthLargest(x,3);
}