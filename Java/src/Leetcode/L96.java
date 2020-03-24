package Leetcode;

public class L96 {
    public static void main(String[] args)
    {
        Solution_96 solution_96 = new Solution_96();
        int[] cases = {2, 3, 4};

        for (int c: cases)
        {
            System.out.println(solution_96.numTrees(c));
        }
    }
}

class Solution_96 {
    public int numTrees(int n) {
        int[] count = new int[n+1];
        count[0] = 1;
        count[1] = 1;

        for (int i = 2; i <= n; i++)
        {
            int temp = 0;
            for (int j = 0; j < i; j++)
            {
                temp += count[j] * count[i-j-1];
            }

            count[i] = temp;
        }

        return count[n];
    }
}
