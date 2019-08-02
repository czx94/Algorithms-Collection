# Manachar Algorithm

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        reference = '@#' + '#'.join(s) + '#$'
        count = [0]*len(reference)
        center = right = 0
        for i in range(1, len(reference) - 1):
            if i < right:
                count[i] = min(right - i, count[2*center - i])
            while reference[i + count[i] + 1] == reference[i - count[i] - 1]:
                count[i] += 1
            if i + count[i] > right:
                center, right = i, i + count[i]

        return sum([(value+1)/2 for value in count])
