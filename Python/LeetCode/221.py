class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        if not matrix[0]:
            return 0

        height = [0] * (len(matrix[0]) + 1)

        area = 0
        for row in matrix:
            container = [-1]
            for j in range(len(row)):
                height[j] = height[j] + 1 if row[j] == '1' else 0

            for j in range(len(row) + 1):
                while height[j] < height[container[-1]]:
                    h = height[container.pop()]
                    w = j - container[-1] - 1
                    area = max(min(h, w) ** 2, area)

                container.append(j)

        return area

if __name__ == '__main__':
    cases = [[[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]]
    solution = Solution()
    for case in cases:
        print(solution.maximalSquare(case))