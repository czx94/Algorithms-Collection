package Leetcode;

import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class L989 {
    public static void main(String[] args)
    {
        int[][] As = {{1, 2, 0, 0}, {2, 7, 4}, {1,2,6,3,0,7,1,7,1,9,7,5,6,6,4,4,0,0,6,3}, {9,9,9,9,9,9,9,9,9,9}};
        int[] Ks = {34, 274, 516, 1};
        Solution_989 solution_989 = new Solution_989();

        for (int i = 0; i < As.length; i++)
        {
            String res = solution_989.addToArrayForm(As[i], Ks[i]).toString();
            System.out.println(res);
        }

    }
}

class Solution_989 {
    public List<Integer> addToArrayForm(int[] A, int K) {
        List<Integer> result = new LinkedList<>();

        int count = A.length - 1;
        while (count >= 0 || K > 0)
        {
            int temp = 0;

            if (count >= 0)
            {
                temp += A[count];
                count -= 1;
            }

            if (K > 0)
            {
                int div = K/10;
                int mod = K%10;
                K = div;
                temp += mod;
            }

            result.add(temp%10);
            K += temp/10;
        }

        Collections.reverse(result);

        return result;
    }
}
