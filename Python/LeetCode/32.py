class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        left = -1
        len_str = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if not stack:
                        len_str = max(len_str, i - left)
                    else:
                        len_str = max(len_str, i - stack[-1])

                else:
                    left = i

        return len_str
