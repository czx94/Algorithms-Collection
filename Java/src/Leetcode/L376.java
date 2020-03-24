package Leetcode;

public class L376 {

}

class Solution_376_0 {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
        {
            return nums.length;
        }

        int [] ups = new int[nums.length];
        int [] downs = new int[nums.length];
        ups[0] = 1;
        downs[0] = 1;

        for (int i = 1; i < nums.length; i++)
        {
            if (nums[i] > nums[i-1])
            {
                ups[i] = downs[i-1] + 1;
                downs[i] = downs[i-1];
            }
            else if (nums[i] < nums[i-1])
            {
                ups[i] = ups[i-1];
                downs[i] = ups[i-1] + 1;
            }
            else
            {
                ups[i] = ups[i-1];
                downs[i] = downs[i-1];
            }
        }

        return Math.max(ups[nums.length-1], downs[nums.length-1]);
    }
}

class Solution_376_1 {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
        {
            return nums.length;
        }

        int up = 1;
        int down = 1;

        for (int i = 1; i < nums.length; i++)
        {
            if (nums[i] > nums[i-1])
            {
                up = down + 1;
            }
            else if (nums[i] < nums[i-1])
            {
                down = up + 1;
            }
        }

        return (up > down) ? up : down;
    }
}