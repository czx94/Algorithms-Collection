class Solution(object):
    # not work ...
    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if nums[mid - 1] > nums[mid] or mid == 0:
                break
            else:
                if nums[mid] > nums[-1]:
                    head = mid + 1
                else:
                    tail = mid - 1

        if target >= nums[mid]:
            head = mid
            tail = len(nums) - 1
        else:
            head = 0
            tail = mid - 1

        while head <= tail:
            mid = (head + tail) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                tail = mid - 1
            else:
                head = mid + 1

        return -1

    def search2(self, nums, target):
        if not nums:
            return -1

        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (head + tail)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[0]:
                if nums[mid] > target >= nums[0]:
                    tail = mid - 1
                else:
                    head = mid + 1
            else:
                if nums[mid] < target <= nums[0]:
                    head = mid + 1
                else:
                    tail = mid - 1

        return -1

    def search3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[head]:
                if nums[head] <= target <= nums[mid]:
                    tail = mid - 1
                else:
                    head = mid + 1

            else:
                if nums[mid] <= target <= nums[tail]:
                    head = mid + 1
                else:
                    tail = mid - 1

        return -1



if __name__ == '__main__':
    solution = Solution()
    cases = [([4,5,6,7,0,1,2], 0), ([1,3],3), ([3, 1], 1)]
    for case in cases:
        print(solution.search2(*case))
        print(case)