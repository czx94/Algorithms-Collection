package Leetcode;

public class L226 {
}


 //Definition for a binary tree node.
class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode(int x) { val = x; }
 }

class Solution_226 {
    public TreeNode invertTree(TreeNode root) {
        if (root != null)
        {
            TreeNode left = root.right;
            TreeNode right = root.left;

            root.right = invertTree(right);
            root.left = invertTree(left);
        }

        return root;
    }
}