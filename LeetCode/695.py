class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.matrix = grid
        row = len(grid)
        if not row:
            return 0
        col = len(grid[0])
        if not col:
            return 0

        max_area = 0

        for i in range(row):
            for j in range(col):
                if self.matrix[i][j] == 1:
                    max_area = max(self.counter(i, j), max_area)

        return self.max_area


    def counter(self, i, j):
        if i < 0 or i >= len(self.matrix) or j < 0 or j >= len(self.matrix[0]) or self.matrix[i][j] != 1:
            return 0

        else:
            self.matrix[i][j] = -1
            top = self.counter(i-1, j)
            down = self.counter(i+1, j)
            left = self.counter(i, j-1)
            right = self.counter(i, j+1)

            return top + down + left + right + 1

