class Solution(object):
    # iterative
    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # dp[i-1][j-1] replace
                    # dp[i][j-1] insert
                    # dp[i-1][j] remove
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]

    # recursive
    def minDistance(self, word1, word2, i=0, j=0, mem={}):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in mem:
            if word1[i] == word2[j]:
                res = self.minDistance(word1, word2, i+1, j+1, mem)
            else:
                replace = self.minDistance(word1, word2, i+1, j+1, mem)
                insert = self.minDistance(word1, word2, i, j+1, mem)
                remove = self.minDistance(word1, word2, i+1, j, mem)
                res = 1 + min(replace, insert, remove)
            mem[(i, j)] = res

        return mem[(i, j)]

if __name__ == '__main__':
    cases = [("intention", "execution")]
    solution = Solution()
    for case in cases:
        print(solution.minDistance(*case))



