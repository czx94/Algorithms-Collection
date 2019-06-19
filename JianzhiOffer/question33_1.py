'''
Whether a list is post travel result of a given bst
leetcode 255
'''

def solution1(nums):
    if not nums:
        return False

    center_node = nums[-1]
    for i in range(len(nums)):
        if nums[i] > center_node:
            break

    for j in range(i, len(nums)):
        if nums[j] <= center_node:
            return False

    if i > 0:
        left = solution1(nums[:i])
    else:
        left = True

    if i < len(nums) - 1:
        right = solution1(nums[i:len(nums)])
    else:
        right = True

    return left and right














