class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        position_dict = dict()
        max_length = 0
        current_length = 0

        for i in range(len(s)):
            if s[i] not in position_dict:
                current_length += 1
            else:
                distance = i - position_dict[s[i]]
                if current_length < distance:
                    current_length += 1
                else:
                    current_length = distance
            position_dict[s[i]] = i
            max_length = max(max_length, current_length)

        return max_length

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_pos = dict()
        length = 0
        base = -1

        for i in range(len(s)):
            ch = s[i]
            if ch in last_pos:
                base = max(base, last_pos[ch])
            last_pos[ch] = i
            length = max(length, i - base)

        return length


if __name__ == '__main__':
    solution = Solution()
    strings = ['arabcacfr', "abba"]
    for string in strings:
        length = solution.lengthOfLongestSubstring2(string)
        print(length)