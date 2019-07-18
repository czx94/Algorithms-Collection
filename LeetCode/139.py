class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)

        for i in range(len(s)):
            for w in wordDict:
                if s[i + 1 - len(w):i + 1] == w and (i - len(w) == -1 or dp[i - len(w)]):
                    dp[i] = True
                    break

        return dp[-1]
