class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0]*len(T)

        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)

        return result