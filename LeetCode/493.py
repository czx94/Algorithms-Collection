'''
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.
'''

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.dfs(nums)[1]


    def dfs(self, nums):
        if len(nums) <= 1:
            return nums, 0

        else:
            left, left_count = self.dfs(nums[:len(nums)//2])
            right, right_count = self.dfs(nums[len(nums)//2:])

            left_index = 0
            right_index = 0
            count = 0

            # count the reversed pairs between left and right
            while left_index < len(left) and right_index < len(right):
                if left[left_index] <= 2 * right[right_index]:
                    left_index += 1
                else:
                    count += len(left) - left_index
                    right_index += 1

            # sort the two pairs
            new_sort = []

            while left and right:
                if left[0] < right[0]:
                    new_sort.append(left.pop(0))
                else:
                    new_sort.append(right.pop(0))

            if left:
                new_sort += left
            elif right:
                new_sort += right

            return new_sort, count + left_count + right_count


if __name__ == '__main__':
    solution = Solution()
    cases = [[1, 3, 2, 3, 1], [2,4,3,5,1]]
    for case in cases:
        print(case)
        print(solution.reversePairs(case))

