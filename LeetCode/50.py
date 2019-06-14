class Solution(object):
    # too slow
    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def non_negative_power(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            else:
                res = 1
                for _ in range(n):
                    res *= x
                return res

        if x == 0:
            return 0

        if n < 0:
            return 1 / non_negative_power(x, -n)
        else:
            return non_negative_power(x, n)

    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def non_negative_power(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            else:
                res = non_negative_power(x, n >> 1)
                res *= res
                if n & 1 == 1:
                    res *= x
                return res

        if x == 0:
            return 0

        if n < 0:
            return 1 / non_negative_power(x, -n)
        else:
            return non_negative_power(x, n)

    # faster
    def myPow3(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow3(x, -n)
        else:
            if n & 1 == 0:
                return self.myPow3(x * x, n >> 1)
            else:
                return x * self.myPow3(x, n - 1)