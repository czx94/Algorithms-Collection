'''
Max number in a sliding window
leetcode 239
'''

# naive, too slow, O(nk)
def solution1(nums, k):
    if not nums:
        return nums

    length = len(nums)
    result = list()
    if k >= length:
        result.append(max(nums))
    else:
        for i in range(length-k+1):
            result.append(max(nums[i: i+k]))

    return result

def solution2(nums, k):
    if not nums:
        return nums

    index = []
    for i in range(k):
        while index and nums[i] >= nums[index[-1]]:
            index.pop()
        index.append(i)

    result = []
    for i in range(k, len(nums)):
        result.append(nums[index[0]])

        while index and nums[i] >= nums[index[-1]]:
            index.pop()
        if index and index[0] <= (i - k):
            index.pop(0)

        index.append(i)

    result.append(nums[index[0]])
    return result

if __name__ == '__main__':
    nums = [2, 3, 4, 2, 6, 2, 5, 1]
    result = solution1(nums, 3)
    print(result)
    result = solution2(nums, 3)
    print(result)