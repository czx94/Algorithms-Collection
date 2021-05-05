class Solution(object):
    # use 223
    def isRectangleOverlap0(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        overlap = max(min(rec1[2], rec2[2]) - max(rec1[0], rec2[0]), 0) * max(
            min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]), 0)

        return (overlap > 0)

    def isRectangleOverlap1(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if min(rec1[2], rec2[2]) <= max(rec1[0], rec2[0]) or min(rec1[3], rec2[3]) <= max(rec1[1], rec2[1]):
            return False
        else:
            return True

if __name__ == '__main__':
    solution = Solution()
    cases = [[[0,0,1,1], [1,0,2,1]], [[0,0,1,1], [1,0,2,1]]]
    for case in cases:
        print(solution.isRectangleOverlap1(*case))