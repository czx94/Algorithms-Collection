class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0

        if nums[0]:
            count_dic = {nums[0]: 1, -nums[0]: 1}
        else:
            count_dic = {0: 2}

        for num in nums[1:]:
            this_count = {}
            for d in count_dic:
                print(num, this_count)
                this_count[d + num] = this_count.get(d + num, 0) + count_dic.get(d, 0)
                this_count[d - num] = this_count.get(d - num, 0) + count_dic.get(d, 0)
            count_dic = this_count

        return count_dic.get(S, 0)


if __name__ == '__main__':
    solution = Solution()
    cases = [([0,0,0,0,0,0,0,0,1], 1), ([1,1,1,1,1], 3)]
    for case in cases:
        print(solution.findTargetSumWays(*case))