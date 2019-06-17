'''
Find the only missing element in a sorted list with len == n formed by n-1 number from 0~n-1
leetcode 268
'''

def solution1(nums):
    head = 0
    tail = len(nums) - 1
    while head <= tail:
        mid = (head + tail)>>1
        if nums[mid] > mid:
            tail = mid - 1
        else:
            head = mid + 1
    return head

if __name__ == '__main__':
    nums = [0,1,2,3,5,6,7,8]
    miss = solution1(nums)
    print(miss)
    nums = [0]
    miss = solution1(nums)
    print(miss)
    nums = [1]
    miss = solution1(nums)
    print(miss)