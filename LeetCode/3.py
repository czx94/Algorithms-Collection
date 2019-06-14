class Solution(object):
    def lengthOfLongestSubstring(self, s):
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