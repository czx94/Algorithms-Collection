'''
Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head = 0
        tail = len(height) - 1
        volume = 0

        while head < tail:
            head_h = height[head]
            head_t = height[tail]
            top = min(head_h, head_t)
            volume = max(volume, top * (tail - head))

            if head_h < head_t:
                head += 1
            else:
                tail -= 1

        return volume

if __name__ == '__main__':
    solution = Solution()
    cases = [[1,8,6,2,5,4,8,3,7], [1, 2]]
    for case in cases:
        print(solution.maxArea(case), case)

