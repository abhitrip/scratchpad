import java.util.*;
class TreeNode{
    protected TreeNode right;
    protected TreeNode left;
    protected int val;
    public TreeNode(int val){
        this.val = val;
        left = null;
        right = null;
    }
    public void insertRightChild(int x)
    {
        TreeNode newnode = new TreeNode(x);
        this.right = newnode;
    }
    public void insertLeftChild(int y)
    {
        TreeNode newnode = new TreeNode(y);
        this.left = newnode;
    }
}


class BinaryTree{
    private TreeNode root;
    public BinaryTree(){
        root = null;
    }
    public void createTree123(){
        root = new TreeNode(5);
        root.insertLeftChild(4);
        root.insertRightChild(8);
        root.left.insertLeftChild(11);
        root.left.left.insertRightChild(2);
        root.left.left.insertLeftChild(7);
        root.right.insertLeftChild(13);
        root.right.insertRightChild(4);
        root.right.right.insertRightChild(1);
        root.right.right.insertLeftChild(5);
    }
    public void inorder(TreeNode root)
    {
        if(root==null)
            return;
        inorder(root.left);
        System.out.println(root.val);
        inorder(root.right);

    }
    public void traversal(){
        inorder(root);
    }
    public TreeNode getRoot(){
        return this.root;
    }

    public void utilityBTPaths(TreeNode root,List<String> res,String path)
    {
        if(root==null)
            return;
        path += Integer.toString(root.val)+"->";
        if((root.left==null)&&(root.right==null))
        {
            path = path.subSequence(0,path.length()-2).toString();
            res.add(path);
        }
        if(root.left!=null)
        {


            utilityBTPaths(root.left,res,path);
        }
        if(root.right!=null)
        {

            utilityBTPaths(root.right,res,path);
        }

        path = path.subSequence(0,path.length()-2).toString();
    }

    public List<String> binaryTreePaths(){
        List<String> res = new ArrayList<>();
        String path = "";
        TreeNode root = getRoot();

        utilityBTPaths(root,res,path);


        System.out.println(res);
        return res;
    }
    public List<List<Integer>> pathSum(TreeNode root,int sum){
        List<List<Integer>> result = new ArrayList<>();
        Stack<TreeNode> stk = new Stack<>();
        Stack<Integer> path = new ArrayList<>();
        stk.push(root);
        int currSum=sum;
        if(root=null)
            return result;

        while(!stk.isEmpty())
        {
            TreeNode curr = stk.pop();
            currSum =  currSum-curr.val;
            path.push(curr.val);
            if((currSum==0)&&(curr.right==null)&&(curr.left==null))
            {
                result.add(new ArrayList(path));
            }
            if(curr.right!=null)
            {
                path.push(curr.)
            }
        }
    }



}

public class allpaths{
    public static void main(String[] args){

        BinaryTree obj = new BinaryTree();
        obj.createTree123();
        obj.traversal();
        /*
        obj.binaryTreePaths();
        */
    }
}
