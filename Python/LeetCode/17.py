class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        for num in digits:
            chs = mapping[num]
            temp = []
            for ch in chs:
                for c in result:
                    temp.append(c + ch)
            result = temp

        return result