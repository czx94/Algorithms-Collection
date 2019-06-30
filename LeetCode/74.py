class Solution(object):
    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False

        for i in range(len(matrix[0]) - 1, -1, -1):
            if matrix[0][i] <= target:
                for j in range(len(matrix)):
                    if matrix[j][i] >= target:
                        small_matrix = matrix[j:][:i + 1]

                        for x in small_matrix:
                            for xy in x:
                                if xy == target:
                                    return True
                return False
            else:
                continue

        return False

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False

        height, width = len(matrix), len(matrix[0])
        low, high = 0, height*width - 1
        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // width][mid % width]
            if val == target:
                return True
            elif val > target:
                high = mid - 1
            else:
                low = mid + 1

        return False


if __name__ == '__main__':
    solution = Solution()
    cases = [([[1]], 2)]
    for case in cases:
        print(solution.searchMatrix2(*case))