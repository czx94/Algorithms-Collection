package Leetcode;

import java.util.Arrays;

public class L324 {
    public static void main(String[] args)
    {
        int[][] cases = {{1, 5, 1, 1, 6, 4}, {1, 3, 2, 2, 3, 1}};
        Solution_324 solution_324 = new Solution_324();

        for (int[] c: cases)
        {
            solution_324.wiggleSort(c);
        }
    }

}

class Solution_324 {
    public void wiggleSort(int[] nums) {
        int[] copy = nums.clone();
        Arrays.sort(copy);

        int mid = (copy.length - 1) >> 1;
        int l = mid, r = copy.length - 1;

        int current = 0;
        while (l>=0 && r>mid)
        {
            nums[current++] = copy[l--];
            nums[current++] = copy[r--];
        }

        while (l>=0)
        {
            nums[current++] = copy[l--];
        }

        while (r>mid)
        {
            nums[current++] = copy[r--];
        }

    }
}