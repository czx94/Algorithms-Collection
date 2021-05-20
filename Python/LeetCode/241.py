class Solution(object):
    def diffWaysToCompute0(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        return [a+b if c=='+' else a-b if c=='-' else a*b
                for i, c in enumerate(expression) if c in '+-*'
                for a in self.diffWaysToCompute0(expression[:i])
                for b in self.diffWaysToCompute0(expression[i+1:])] \
                or [int(expression)]

    def diffWaysToCompute1(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        result = list()
        for i, item in enumerate(expression):
            if item in '+-*':
                left = self.diffWaysToCompute1(expression[:i])
                right = self.diffWaysToCompute1(expression[i+1:])
                result.extend(self.group_calculate(left, right, item))

        return result or [int(expression)]

    def group_calculate(self, left, right, operator):
        result = list()
        if operator == '+':
            for x in left:
                for y in right:
                    result.append(x+y)
        elif operator == '-':
            for x in left:
                for y in right:
                    result.append(x-y)
        else:
            for x in left:
                for y in right:
                    result.append(x*y)

        return result




if __name__ == '__main__':
    cases = ["2-1-1", "2*3-4*5"]
    solution = Solution()
    for case in cases:
        print(solution.diffWaysToCompute1(case))