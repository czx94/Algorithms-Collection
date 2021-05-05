class Solution(object):
    def isodd(self, num):
        return num&1

    # too slow
    def numberOfSteps0(self, num):
        """
        :type num: int
        :rtype: int
        """
        res_list = [0]
        for i in range(1, num+1):
            if not self.isodd(i):
                res_list.append(res_list[(i+1)//2] + 1)
            else:
                res_list.append(res_list[-1] + 1)

        return res_list[-1]

    def numberOfSteps1(self, num):
        count = 0
        while num != 0:
            if self.isodd(num):
                num -= 1
            else:
                num /= 2

            count += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    num_list = [14, 8, 2, 1, 3]
    for num in num_list:
        print(solution.numberOfSteps(num))

