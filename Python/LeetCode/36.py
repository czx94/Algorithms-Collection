from functools import reduce
class Solution(object):
    # solution one is ordinary
    def isValidSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isValidBox(board) and self.isValidCollum(board) and self.isValidRow(board)

    def isValidCollum(self, board):
        for vector in zip(*board):
            if not self.isValid(vector):
                return False

        return True

    def isValidRow(self, board):
        for vector in board:
            if not self.isValid(vector):
                return False

        return True

    def isValidBox(self, board):
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                vector = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValid(vector):
                    return False

        return True

    def isValid(self, vector):
        vector = [i for i in vector if i != '.']
        return len(set(vector)) == len(vector)


    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        elements = []
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value != '.':
                    elements += [(i, value), (value, j), (i // 3, j // 3, value)]

        return len(set(elements)) == len(elements)

if __name__ == '__main__':
    solution = Solution()
    case = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(solution.isValidSudoku2(case))