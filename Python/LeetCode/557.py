class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sequences = s.split(' ')
        string = ' '.join([s[::-1] for s in sequences])

        return string