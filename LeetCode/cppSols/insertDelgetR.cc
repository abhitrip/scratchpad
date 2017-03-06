#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <vector>
using namespace std;

class RandomizedSet {

private:
    unordered_map<int,int> posLoc;
    vector<int> vec;
public:
    /** Initialize your data structure here. */
    
    RandomizedSet() {
       
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        auto it = posLoc.find(val);
        if (it!= posLoc.end())
            {
                return false;
            }
        vec.push_back(val);
        posLoc[val] = vec.size()-1;
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(posLoc.find(val)!=posLoc.end())
            {
                int idx = posLoc[val];
                int last = vec.back();
                vec.pop_back();
                vec[idx] = last;
                posLoc.erase(val);
                
                  
                            
                return true;
            }
            return false;
         }
    
    /** Get a random element from the set. */
    int getRandom() {
        int randIdx = rand()%vec.size();
        return vec[randIdx];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
 int main(int argc,char* argv[])
 {

 }