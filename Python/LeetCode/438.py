class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_count = dict()
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1
        s_count = {}
        for ch in s[:len(p) - 1]:
            s_count[ch] = s_count.get(ch, 0) + 1

        indexes = []
        for i in range(len(p) - 1, len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            if s_count == p_count:
                indexes.append(i + 1 - len(p))
            s_count[s[i + 1 - len(p)]] -= 1
            if s_count[s[i + 1 - len(p)]] == 0:
                del s_count[s[i + 1 - len(p)]]

        return indexes
