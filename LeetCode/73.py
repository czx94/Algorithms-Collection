class Solution(object):
    def setZeroes1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        if not matrix[0]:
            return matrix

        row_stat = [1] * len(matrix)
        col_stat = [1] * len(matrix[0])

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    row_stat[i] = 0
                    col_stat[j] = 0

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if not row_stat[i] or not col_stat[j]:
                    matrix[i][j] = 0

    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        if not matrix[0]:
            return matrix

        row_len = len(matrix)
        col_len = len(matrix[0])

        row_zero = False
        col_zero = False
        for i in range(row_len):
            if matrix[i][0] == 0:
                row_zero = True
        for i in range(col_len):
            if matrix[0][i] == 0:
                col_zero = True

        if row_len > 1 and col_len > 1:
            for i in range(1, row_len):
                for j in range(1, col_len):
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
            for i in range(1, row_len):
                if matrix[i][0] == 0:
                    for j in range(1, col_len):
                        matrix[i][j] = 0

            for j in range(1, col_len):
                if matrix[0][j] == 0:
                    for i in range(1, row_len):
                        matrix[i][j] = 0

        if row_zero:
            for i in range(row_len):
                matrix[i][0] = 0

        if col_zero:
            for i in range(col_len):
                matrix[0][i] = 0


if __name__ == '__main__':
    solution = Solution()
    cases = [[[0],[1]], [[0,1,2,0],[3,4,5,2],[1,3,1,5]]]
    for case in cases:
        solution.setZeroes2(case)