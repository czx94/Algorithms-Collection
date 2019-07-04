'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''


class Solution(object):
    # stupid merge
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        elif len(strs) == 1:
            return strs[0]

        else:
            s1 = self.longestCommonPrefix1(strs[:len(strs) // 2])
            s2 = self.longestCommonPrefix1(strs[len(strs) // 2:])

            common = ''
            for i in range(min(len(s1), len(s2))):
                if s1[i] == s2[i]:
                    common += s1[i]
                else:
                    break

            return common

    # cmp to the shortest, faster
    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        strs.sort(key=len)

        for i, ch in enumerate(strs[0]):
            for str in strs[1:]:
                if str[i] != ch:
                    return strs[0][:i]

        return strs[0]