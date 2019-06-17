'''
A given list is monotone increasing，every element is a int and unique, find a element with its index equals to its value
https://www.acwing.com/problem/content/65/?time=1560688667158
'''

def solution1(nums):
    if not nums:
        return -1

    head = 0
    tail = len(nums) - 1

    while(head <= tail):
        mid = (tail + head) >> 1
        if nums[mid] == mid:
            return mid

        if nums[mid] > mid:
            tail = mid - 1
        else:
            head = mid + 1

    return -1

if __name__ == '__main__':
    nums = [-3, -1, 1, 3, 5]
    result = solution1(nums)
    print(result)