class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_len = len(grid)
        if not row_len:
            return 0
        col_len = len(grid[0])
        if not col_len:
            return 0

        for i in range(1, row_len):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, col_len):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, row_len):
            for j in range(1, col_len):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]