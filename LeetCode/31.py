class Solution(object):
    def nextPermutation1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        if len(nums) < 2:
            return nums[::-1]

        tail = len(nums) - 1
        head = -1

        # find the first descending pair from the tail
        while tail > 0:
            if nums[tail-1] < nums[tail]:
                head = tail-1
                break
            tail -= 1

        # find the first bigger number than the head from the tail
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[head]:
                print(head, i)
                nums[head], nums[i] = nums[i], nums[head]
                nums[head + 1:] = sorted(nums[head + 1:])
                return nums

    def nextPermutation2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        if len(nums) < 2:
            return nums[::-1]

        mark = tail = len(nums) - 1
        while mark>=0 and nums[mark - 1] >= nums[mark]:
            mark -= 1
        if mark == 0:
            nums.reverse()
            return nums

        head = mark - 1  # find the last "ascending" position
        while nums[tail] <= nums[head]:
            tail -= 1
        nums[head], nums[tail] = nums[tail], nums[head]
        nums[head + 1:] = sorted(nums[head + 1:])
        return nums


if __name__ == '__main__':
    solution = Solution()
    cases = [[1,3,2],[2,3,1],[3,1,2],[3,2,1],[1,2,3]]
    for case in cases:
        print('######')
        print('input:',case)
        # print('output1:',solution.nextPermutation1(case))
        print('output2:',solution.nextPermutation2(case))
        print('######')
