class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        if not board[0]:
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.dfs(board, word, i, j):
                    return True

        return False


    def dfs(self, board, word, i, j):
        if not word:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] != word[0]:
            return False

        tmp = board[i][j]
        board[i][j] = '0'
        top = self.dfs(board, word[1:], i-1, j)
        bottom = self.dfs(board, word[1:], i+1, j)
        left = self.dfs(board, word[1:], i, j-1)
        right = self.dfs(board, word[1:], i, j+1)

        board[i][j] = tmp
        return top or bottom or left or right




