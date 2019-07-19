'''
Path in a matrix
leetcode 79
'''
import numpy as np

def solution1(board, word):
    paths = []
    neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # find the positions of the first letter
    start_points = []
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i][j] == word[0]:
                start_points.append((i, j))

    if not start_points:
        return False

    for start_point in start_points:
        # to mark a point is visited or not
        mark_matrix = np.zeros(board.shape)
        current_path = [[start_point, 0]]

        while current_path and len(current_path) < len(word):
            if current_path[-1][1] == 4:
                current_path.pop()
                print('Back')
            last_point = current_path[-1][0]
            neighbor_coord = neighbors[current_path[-1][1]]
            current_path[-1][1] += 1
            column = neighbor_coord[1] + last_point[1]
            row = neighbor_coord[0] + last_point[0]

            if 0 <= column < board.shape[1] and 0 <= row < board.shape[0]:
                if mark_matrix[row][column] == 0 and board[row][column] == word[len(current_path)]:
                    current_path.append([(row, column), 0])
                    mark_matrix[row][column] = 1

        if len(current_path) == len(word):
            paths.append(current_path)

    return paths

if __name__ == '__main__':
    matrix = np.array([['a', 'b', 't', 'g'],
                       ['c', 'f', 'c', 's'],
                       ['j', 'd', 'e', 'h']])
    word = 'btce'
    print(matrix, word)
    print(solution1(matrix, word))

    matrix = np.array([['t', 'b', 't', 'g'],
                       ['c', 't', 'c', 's'],
                       ['j', 'd', 'e', 'h']])
    word = 'btce'
    print(matrix, word)
    print(solution1(matrix, word))