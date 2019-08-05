'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(x, y):
            if x == -1 or x == row or y == -1 or y == col or board[x][y] != 'O':
                return

            else:
                board[x][y] = 'Y'
                dfs(x, y-1)
                dfs(x, y+1)
                dfs(x-1, y)
                dfs(x+1, y)

        row = len(board)
        if not row:
            return 0
        col = len(board[0])
        if not col:
            return 0

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == (row-1) or j == (col-1)) :
                    dfs(i, j)
    
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'
        print(board)

if __name__ == '__main__':
    cases = [[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]], [["O","O"],["O","O"]]]
    solution = Solution()
    for case in cases:
        solution.solve(case)
