package Leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class L1 {
    public static void main(String[] args)
    {
        int[][] cases = {{2, 7, 11, 15}};
        int[] targets = {9};
        Solution_1 solution = new Solution_1();

        for (int ind = 0; ind < cases.length; ind++)
        {
            int [] result = solution.twoSum(cases[ind], targets[ind]);
            System.out.println(Arrays.toString(result));
        }
    }
}

class Solution_1 {
    public int[] twoSum(int[] nums, int target) {
        Map dict = new HashMap();
        int[] res = null;

        for (int i = 0; i < nums.length; i++)
        {
            if (dict.containsKey(nums[i]))
            {
                res = new int[] {i, (int) dict.get(nums[i])};
                return res;
            }
            dict.put(target - nums[i], i);
        }

        return res;
    }
}