'''
leetcode 846
'''

def solution1(nums):
    if not nums:
        return

    nums.sort()

    count_zero = 0
    count_gap = 0

    # count zeros
    for num in nums:
        if num == 0:
            count_zero += 1
    assert count_zero <= 2

    # count gaps
    head = count_zero
    tail = head + 1

    while tail < len(nums):
        if nums[head] == nums[tail]:
            return False

        else:
            count_gap += nums[tail] - nums[head] - 1
            head, tail = tail, tail + 1

    return count_zero >= count_gap


if __name__ == '__main__':
    nums = [[0, 1, 3, 4, 5], [1, 1, 2, 3, 4], [2, 3, 0, 4, 5]]
    for num in nums:
        result = solution1(num)
        print(result, num)
