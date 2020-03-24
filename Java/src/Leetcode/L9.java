package Leetcode;

public class L9 {
    public static void main(String[] args)
    {
        int[] cases = {10, 101, 200, -101};

        Solution_9 solution = new Solution_9();

//        for (int i = 0; i < cases.length; i++)
        for (int c: cases)
        {
            System.out.println(solution.isPalindrome(c));
        }
    }
}

class Solution_9 {
    public boolean isPalindrome(int x) {
        if (x < 0)
        {
            return false;
        }
        else if (x < 10)
        {
            return true;
        }

        char[] s = String.valueOf(x).toCharArray();
        for (int i = 0; i < s.length/2; i++)
        {
            if (s[i] != s[s.length-i-1])
            {
                return false;
            }
        }
        return true;

    }
}
