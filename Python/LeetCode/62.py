import numpy as np
import math


class Solution(object):
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0

        count = np.zeros((m, n))

        for i in range(m):
            count[i][0] = 1
        for j in range(n):
            count[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                count[i][j] = count[i - 1][j] + count[i][j - 1]

        return count[-1][-1]

    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return math.factorial(n+m-2)/math.factorial(n-1)/math.factorial(m-1)
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 2))