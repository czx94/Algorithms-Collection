class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_str = ''
        self.s = s
        for i in range(len(s)):
            max_str = max(max_str, self.palindrome(i, i), self.palindrome(i, i + 1), key=len)

        return max_str

    def palindrome(self, head, tail):
        while head >= 0 and tail < len(self.s) and self.s[head] == self.s[tail]:
            tail += 1
            head -= 1

        return self.s[head+1:tail]

if __name__ == '__main__':
    solution = Solution()
    cases = ["babad", "cbbd"]
    for case in cases:
        print(case)
        print(solution.longestPalindrome(case))