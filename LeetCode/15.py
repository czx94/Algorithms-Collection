class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            head = i + 1
            tail = len(nums) - 1
            while head < tail:
                s = nums[i] + nums[head] + nums[tail]
                if s == 0:
                    results.append([nums[i], nums[head], nums[tail]])
                    while head < tail and nums[head] == nums[head + 1]:
                        head += 1
                    while head < tail and nums[tail] == nums[tail - 1]:
                        tail -= 1
                    head += 1
                    tail -= 1
                elif s < 0:
                    head += 1
                else:
                    tail -= 1

        return results