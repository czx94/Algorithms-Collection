class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = {}

        for ch in J:
            count[ch] = 0

        for ch in S:
            if ch in count:
                count[ch] += 1

        return sum([value for ch, value in count.items()])