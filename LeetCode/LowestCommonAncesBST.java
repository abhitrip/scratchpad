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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root==null)
            return null;
        int max = Math.max(p.val,q.val);
        int min = Math.min(p.val,q.val);
        if(root.val<=max && root.val>=min)
            return root;
        if(root.val>=max)
            return lowestCommonAncestor(root.left,p,q);
        return lowestCommonAncestor(root.right,p,q);
    }
}
