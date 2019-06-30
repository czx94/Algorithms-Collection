class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                tail = mid - 1
            else:
                head = mid + 1

        return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.search([-1, 0, 5], 0))