class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.point_avail = [[list(range(1, 10))] * 9] * 9
        visit = [[1] * 9] * 9
        # check out the situation
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                # check if has been filled
                if val == '.':
                    visit[i][j] = 0
                # eliminer avalability
                else:
                    self.vary_avail(i, j, val)

        print(visit, self.point_avail)

    def vary_avail(self, i, j, val):
        for col_ind in range(9):
            print(val, self.point_avail[i][col_ind])
            if val in self.point_avail[i][col_ind]:
                self.point_avail[i][col_ind].remove(val)

        for row_ind in range(9):
            if val in self.point_avail[row_ind][j]:
                self.point_avail[row_ind][j].remove(val)

        box_row = i // 3
        box_cod = j // 3
        for row_ind in range(box_row, box_row+3):
            if row_ind != i:
                for col_ind in range(box_cod, box_cod+3):
                    if col_ind != j and val in self.point_avail[row_ind][col_ind]:
                        self.point_avail[row_ind][col_ind].remove(val)


if __name__ == '__main__':
    case = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    print(solution.solveSudoku(case))

