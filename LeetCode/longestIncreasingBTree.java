/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    int max = 0;
    public void longestUtil(TreeNode root, int target, int curr)
    {
        if(root==null)
            return ;
        
        if(root.val==target)
            curr+=1;
        else
            curr=1;
        
        max = Math.max(curr,max);
        longestUtil(root.left,root.val+1,curr);
        longestUtil(root.right,root.val+1,curr);
        
        
        
    }
    public int longestConsecutive(TreeNode root) {
        if(root==null)
            return max;
        
        
        int curr = max;
        longestUtil(root,0,curr);
        return max;
        
        
    }
}