class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        if not grid[0]:
            return 0

        count = 0
        self.grid = grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '1':
                    self.dfs(i, j)
                    count += 1

        return count

    def dfs(self, i, j):
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]) or self.grid[i][j] != '1':
            return

        self.grid[i][j] = '#'
        self.dfs(i, j-1)
        self.dfs(i, j+1)
        self.dfs(i-1, j)
        self.dfs(i+1, j)