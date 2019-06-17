'''
Sum equal s
leetcode 1
'''

# hashmap
def solution1(nums, s):
    hashmap = {}
    for num in nums:
        if num not in hashmap:
            hashmap[s-num] = num

        else:
            return num, hashmap[num]

    return None

# two pointers
def solution2(nums, s):
    head = 0
    tail = len(nums) - 1

    while head < tail:
        two_sum = nums[head] + nums[tail]
        if two_sum == s:
            return nums[head], nums[tail]
        elif two_sum > s:
            tail -= 1
        else:
            head += 1

    return None


if __name__ == '__main__':
    nums = [1, 2, 4, 7, 11, 15]
    result = solution1(nums, 15)
    print(result)
    result = solution2(nums, 15)
    print(result)