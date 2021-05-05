package Leetcode;

import java.util.Arrays;

public class L654 {
}

class Solution_654 {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if (nums.length == 0)
        {
            return null;
        }

        int[] val_int = valInd(nums);
        int val = val_int[0];
        int ind = val_int[1];

        TreeNode root = new TreeNode(val);

        root.left = constructMaximumBinaryTree(Arrays.copyOfRange(nums, 0, ind));
        root.right = constructMaximumBinaryTree(Arrays.copyOfRange(nums, ind + 1, nums.length));

        return root;
    }

    private int[] valInd(int[] nums)
    {
        int ind = 0;
        int max = nums[ind];

        for (int i = 1; i < nums.length; i++)
        {
            if (nums[i] > max)
            {
                max = nums[i];
                ind = i;
            }
        }

        return new int[] {max, ind};
    }
}

