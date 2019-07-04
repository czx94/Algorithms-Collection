'''
Given a collection of intervals, merge all overlapping intervals.

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals

        cmp = lambda x: x[0]
        intervals.sort(key=cmp)

        i = 1
        while i < len(intervals):
            while i < len(intervals) and intervals[i - 1][-1] >= intervals[i][0]:
                intervals[i - 1][-1] = max(intervals[i][-1], intervals[i - 1][-1])
                intervals.pop(i)

            i += 1

        return intervals

if __name__ == '__main__':
    cases = [[[1,3],[2,6],[8,10],[15,18]], [[1,4],[4,5]]]
    solution = Solution()
    for case in cases:
        print(solution.merge(case))



