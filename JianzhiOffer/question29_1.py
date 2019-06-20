'''
Spiral Matrix
leetcode 54
'''

def solution1(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = list(map(list,zip(*matrix)))[::-1]

    return result

if __name__ == '__main__':
    inputs = [
            [
             [ 1, 2, 3 ],
             [ 4, 5, 6 ],
             [ 7, 8, 9 ]
            ],
            [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
            ]
            ]

    for matrix in inputs:
        print(solution1(matrix))