'''
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Input: k = 3, n = 7
Output: [[1,2,4]]
'''

import copy

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = list()
        current = list()
        candidates = list(range(1, 10))
        self.dfs(k, n, current, candidates)

        return self.result

    def dfs(self, k, n, current, candidates):
        if k < 0 or n < 0:
            return

        if k == 0 and n == 0:
            self.result.append(current)
            return

        for i in range(len(candidates)):
            temp = copy.deepcopy(current)
            temp.append(candidates[i])
            self.dfs(k - 1, n - candidates[i], temp, candidates[i+1:])

if __name__ == '__main__':
    pass
        
