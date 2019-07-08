class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [['', 1]]
        for ch in s:
            if ch.isdigit():
                num = int(ch)
            elif ch == '[':
                stack.append(['', num])
            elif ch == ']':
                string, times = stack.pop()
                stack[-1][0] += string * times
            else:
                stack[-1][0] += ch

        return stack[0][0]

if __name__ == '__main__':
    cases = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]
    solution = Solution()
    for case in cases:
        print(solution.decodeString(case))