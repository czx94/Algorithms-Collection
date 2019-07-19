class Solution(object):
    def sortedSquares1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        positive = []
        negative = []
        for num in A:
            if num < 0:
                negative.append(num * num)
            else:
                positive.append(num * num)

        result = []
        negative.reverse()
        while positive and negative:
            if positive[0] < negative[0]:
                result.append(positive.pop(0))
            else:
                result.append(negative.pop(0))

        if positive:
            result += positive
        elif negative:
            result += negative

        return result

    # two pointers
    def sortedSquares2(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        head = 0
        tail = len(A) - 1

        while head <= tail:
            if abs(A[tail]) > abs(A[head]):
                result.append(A[tail]*A[tail])
                tail -= 1
            else:
                result.append(A[head]*A[head])
                head += 1

        return result[::-1]

if __name__ == '__main__':
    solution = Solution()
    cases = [[-1]]
    for case in cases:
        print(case)
        print(solution.sortedSquares2(case))