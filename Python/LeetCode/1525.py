class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_dict = dict()
        for c in s:
            count_dict[c] = count_dict.get(c, 0) + 1

        count = 0
        rest_dict = dict()
        for c in s:
            count_dict[c] -= 1
            rest_dict[c] = rest_dict.get(c, 0) + 1
            if count_dict[c] == 0:
                del count_dict[c]

            if len(count_dict) == len(rest_dict):
                count += 1
            elif len(count_dict) < len(rest_dict):
                break

        return count
