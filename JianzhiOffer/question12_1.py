'''
Path in a matrix
leetcode 79
'''
import numpy as np

def solution1(matrix, target):
    paths = []
    neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # find the positions of the first letter
    start_points = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == target[0]:
                start_points.append((i, j))

    if not start_points:
        return False

    for start_point in start_points:
        # to mark a point is visited or not
        mark_matrix = np.zeros(matrix.shape)
        current_path = [[start_point, 0]]

        while current_path and len(current_path) < len(target):
            if current_path[-1][1] == 4:
                current_path.pop()
                print('Back')
            last_point = current_path[-1][0]
            neighbor_coord = neighbors[current_path[-1][1]]
            current_path[-1][1] += 1
            column = neighbor_coord[1] + last_point[1]
            row = neighbor_coord[0] + last_point[0]

            if 0 <= column < matrix.shape[1] and 0 <= row < matrix.shape[0]:
                if mark_matrix[row][column] == 0 and matrix[row][column] == target[len(current_path)]:
                    current_path.append([(row, column), 0])
                    mark_matrix[row][column] = 1

        if len(current_path) == len(target):
            paths.append(current_path)

    return paths

if __name__ == '__main__':
    matrix = np.array([['a', 'b', 't', 'g'],
                       ['c', 'f', 'c', 's'],
                       ['j', 'd', 'e', 'h']])
    target = 'btce'
    print(matrix, target)
    print(solution1(matrix, target))

    matrix = np.array([['t', 'b', 't', 'g'],
                       ['c', 't', 'c', 's'],
                       ['j', 'd', 'e', 'h']])
    target = 'btce'
    print(matrix, target)
    print(solution1(matrix, target))