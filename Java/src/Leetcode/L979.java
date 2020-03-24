package Leetcode;

public class L979 {
    public static void main(String[] args)
    {
        Solution_979 solution_979 = new Solution_979();
    }
}

class Solution_979 {
    public int distributeCoins(TreeNode root) {
        return helper(root)[0];
    }

    private int[] helper(TreeNode root)
    {
        if (root == null)
        {
            return new int[]{0,0};
        }

        int[] left = helper(root.left);
        int[] right = helper(root.right);

        int accumulation = left[1] + right[1] + root.val - 1;
        int absolute = Math.abs(left[1]) + Math.abs(right[1]) + left[0] + right[0];

        return new int[]{absolute, accumulation};
    }
}

