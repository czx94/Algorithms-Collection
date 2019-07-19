class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = dict()
        result = ''

        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1

        sorted_freq = [(ch, f) for ch, f in counter.items()]
        sorted_freq.sort(key=lambda x: x[1])
        sorted_freq.reverse()

        for ch, f in sorted_freq:
            result += ch * f

        return result