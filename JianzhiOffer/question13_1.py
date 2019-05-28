'''
Robots movement range
'''
# dfs + back track
def solution1(start_point, threshold):
    def is_available(point, threshold):
        row, column = str(point[0]), str(point[1])

        the_sum = 0
        for num in row + column:
            the_sum += int(num)

        if the_sum <= threshold:
            return True
        else:
            return False

    available_points = [start_point]
    current_path = [[start_point, 0]]
    neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while current_path:
        if current_path[-1][1] == 4:
            current_path.pop()
            continue

        last_point = current_path[-1][0]
        neighbor_coord = neighbors[current_path[-1][1]]
        current_path[-1][1] += 1
        column = neighbor_coord[1] + last_point[1]
        row = neighbor_coord[0] + last_point[0]

        # judge if this point is available
        if row >= 0 and column >= 0 and is_available((row, column), threshold) and [row, column] not in available_points:
            available_points.append([row, column])
            current_path.append([(row, column), 0])

    return len(available_points)

if __name__ == '__main__':
    start_point = [0,0]
    threshold = 10
    print(solution1(start_point, threshold))

