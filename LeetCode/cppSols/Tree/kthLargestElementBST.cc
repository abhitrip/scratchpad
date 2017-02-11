// /**
//  * Definition for a binary tree node.
//  * struct TreeNode {
//  *     int val;
//  *     TreeNode *left;
//  *     TreeNode *right;
//  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//  * };
//  */
#include <iostream>
#include <stack>
using namespace std;
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> stk;
        TreeNode* curr = root;
        if (!root) return -1;
        
        while(curr||!stk.empty())
        {
            while(curr)
            {
                stk.push(curr);
                curr=curr->left;
            }
            curr = stk.top();
            stk.pop();
            
            k-=1;
            
            if(k==0)
                return curr->val;
            curr = curr->right;    
        }
    }
};