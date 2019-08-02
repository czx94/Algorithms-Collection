class Solution(object):
    # TLE
    def subarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1

        return count

    def subarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = {0:1}
        total_sum = 0
        count = 0
        for num in nums:
            total_sum += num
            count += counter.get(total_sum - k, 0)
            counter[total_sum] = counter.get(total_sum, 0) + 1

        return count

