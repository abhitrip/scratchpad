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

    public List<TreeNode> generate(int start,int end)
    {
        List<TreeNode> heads = new ArrayList<>();
        if(start>end)
        {
            heads.add(null);
            return heads;
        }

        for(int i=start;i<=end;i++)
        {
            List<TreeNode> left = generate(start,i-1);
            List<TreeNode> right = generate(i+1,end);

            for(TreeNode l:left)
            {
                for(TreeNode r:right)
                {

                    TreeNode head = new TreeNode(i);
                    head.left = l;
                    head.right = r;
                    heads.add(head);

                }
            }
        }


        return heads;


    }

    public List<TreeNode> generateTrees(int n) {
        if(n==0)
            return new ArrayList<TreeNode>();
        return generate(1,n);
    }
}
