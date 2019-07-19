class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.results = []

        self.generate('', n, n)

        return self.results

    def generate(self, p, l, r):
        if not r:
            self.results.append(p)

        if l:
            self.generate(p + '(', l - 1, r)
        if l < r:
            self.generate(p + ')', l, r - 1)
