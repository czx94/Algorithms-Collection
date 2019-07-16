class Solution(object):
    # dp solution
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        freq = [1, 1]
        if n > 1:
            for i in range(2, n + 1):
                res = 0
                for j in range(i):
                    res += freq[j] * freq[i - j - 1]
                freq.append(res)

        return freq[n]

