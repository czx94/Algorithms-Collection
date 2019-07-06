class Solution(object):
    def isUgly1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        uglys = [1, 2, 3, 4, 5]
        if num < 6:
            return len([n for n in uglys if n <= num])

        ind_2 = 0
        ind_3 = 0
        ind_5 = 0
        while uglys[-1] < num:
            while uglys[ind_2] * 2 <= uglys[-1]:
                ind_2 += 1

            while uglys[ind_3] * 3 <= uglys[-1]:
                ind_3 += 1

            while uglys[ind_5] * 5 <= uglys[-1]:
                ind_5 += 1

            uglys.append(min([uglys[ind_5] * 5, uglys[ind_3] * 3, uglys[ind_2] * 2]))

        return uglys[-1] == num

    # stupid but faster
    def isUgly2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num:
            return None

        while not num & 1:
            num >>= 1
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5

        return num == 1

if __name__ == '__main__':
    solution = Solution()
    print(solution.isUgly1(6))


