class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        if not row:
            return 0
        col = len(matrix[0])
        if not col:
            return 0

        heights = [0] * (col + 1)
        area = 0

        for row in matrix:
            stack = [-1]
            for j in range(len(row)):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            for j in range(len(row) + 1):
                while heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - 1 - stack[-1]
                    area = max(area, h * w)
                stack.append(j)

        return area
