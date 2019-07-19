class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        count = 0
        base = 1
        num = n
        while num:
            remainder = num % 10
            num = num // 10
            count += (num * base)
            if remainder == 1:
                count += (n % base + 1)
            elif remainder > 1:
                count += base
            base *= 10

        return count
