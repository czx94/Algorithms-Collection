class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for p in s:
            if not stack or pair.get(stack[-1], 0) != p:
                stack.append(p)
            else:
                stack.pop()

        return stack == []