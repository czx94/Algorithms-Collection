class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sequences = s.strip().split()
        return ' '.join(sequences[::-1])



if __name__ == '__main__':
    solution = Solution()
    cases = ["a good   example", "the sky is blue", "  hello world!  "]
    for case in cases:
        print(solution.reverseWords(case))