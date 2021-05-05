class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        result = list()

        for n in num:
            while k and result and result[-1] > n:
                result.pop()
                k -= 1
            result.append(n)

        return ''.join(result[:-k or None]).lstrip('0') or '0'

if __name__ == '__main__':
    solution = Solution()
    cases = [("1432219", 3), ("10200", 1), ("10", 2), ('10', 1), ("112", 1)]
    for case in cases:
        print(solution.removeKdigits(*case))