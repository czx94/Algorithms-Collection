'''
Given a non-negative index k where k ≤ 33,
return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Input: 3
Output: [1,3,3,1]
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        this_row = [1]
        for i in range(rowIndex):
            this_row = [1] + list(map(lambda x: x[0] + x[1], zip(this_row, this_row[1:] + [0])))

        return this_row
    
if __name__ == '__main__':
    cases = [0, 1, 3, 5]
    solution = Solution()
    for case in cases:
        print(solution.getRow(case))