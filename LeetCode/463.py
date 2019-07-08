class Solution(object):
    def islandPerimeter1(self, grid):
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

        for i in range(row):
            for j in range(col):
                if self.matrix[i][j] == 1:
                    return self.counter(i, j)[0]

        return 0

    def counter(self, i, j):
        if self.matrix[i][j] != 1:
            return 0, self.matrix[i][j]

        else:
            self.matrix[i][j] = -1
            if i > 0:
                top, t = self.counter(i - 1, j)
            else:
                top, t = 0, 0

            if i < len(self.matrix) - 1:
                down, d = self.counter(i + 1, j)
            else:
                down, d = 0, 0

            if j > 0:
                left, l = self.counter(i, j - 1)
            else:
                left, l = 0, 0

            if j < len(self.matrix[0]) - 1:
                right, r = self.counter(i, j + 1)
            else:
                right, r = 0, 0

            base = 4
            neighbors = [t, d, l, r]
            for n in neighbors:
                if n != 0:
                    base -= 1

            return top + down + left + right + base, -1

    def islandPerimeter2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        if not row:
            return 0
        col = len(grid[0])
        if not col:
            return 0

        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        cur_x, cur_y = i + x, j + y
                        if cur_x < 0 or cur_y < 0 or cur_x == row or cur_y == col or grid[cur_x][cur_y] == 0:
                            count += 1


        return count

if __name__ == '__main__':
    cases = [[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]]
    solution = Solution()
    for case in cases:
        print(solution.islandPerimeter2(case))
