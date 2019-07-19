class Solution(object):
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = dict()
        for i in range(len(s)):
            ch = s[i]
            if ch not in freq:
                freq[ch] = i
            else:
                freq[ch] = -1

        valid_freq = [f for ch, f in freq.items() if f != -1]
        return min(valid_freq) if valid_freq else -1

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = dict()

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1