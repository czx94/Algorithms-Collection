class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        miss = list(t)
        index = dict()
        for ch in miss:
            index[ch] = []

        start = 0
        end = len(s) - 1
        for i in range(len(s)):
            ch = s[i]
            if ch in t:
                if ch not in miss and index[ch] != []:
                    index[ch].pop(0)
                elif ch in miss:
                    miss.remove(ch)
                index[ch].append(i)

                if miss == []:
                    maximum = max([v[-1] for v in index.values()])
                    minimum = min([v[0] for v in index.values()])
                    if maximum - minimum + 1 < end - start + 1:
                        start = minimum
                        end = maximum

        if miss != []:
            return ''
        else:
            return s[start: end + 1]

if __name__ == '__main__':
    cases = [("ADOBECODEBANC", "ABC")]
    solution = Solution()
    for case in cases:
        print(solution.minWindow(*case))