class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        # so important
        heights.append(0)
        area = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1]
                area = max(area, h*w)
            stack.append(i)

        return area



if __name__ == '__main__':
    solution = Solution()
    cases = [[4,2,0,3,2,4,3,4], [2,1,5,6,2,3], [1,2,3,4,5,1]]
    for case in cases:
        print(solution.largestRectangleArea(case))