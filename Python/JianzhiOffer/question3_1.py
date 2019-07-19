'''
Find the repeated numbers in a list

List l has a length of n, all its elements are integers between 0 and n - 1.
Some of the elements are repeated, but we don't know how many of them are and for how many times
Objective is to find any of the repeated numbers

leetcode 287
'''
import numpy as np

'''
using hashtable to record the frequence of each element
time complexity O(n), space complexity O(n)
'''
def solution1(nums):
    hash_table = dict()
    for element in nums:
        if element not in hash_table:
            hash_table[element] = 1
        else:
            hash_table[element] += 1

    for key, value in hash_table.items():
        if value > 1:
            print(key, value)

'''
sort the array, then find the repeat ones
time complexity O(nlgn), space complexity O(1)
'''
def solution2(nums):
    nums = sorted(nums)
    index = 0

    while index < len(nums) - 1:
        if nums[index] == nums[index+1]:
            while index < len(nums) - 1 and nums[index] == nums[index+1]:
                index += 1
        index += 1


'''
exchange each element with the element in the index of its value
'''
def solution3(nums):
    print(nums)
    duplicated_list = list()
    for index in range(len(nums)):
        while nums[index] != index:
            if nums[index] == nums[nums[index]]:
                if nums[index] not in duplicated_list:
                    duplicated_list.append(nums[index])
                break
            else:
                temp = nums[index]
                nums[index] = nums[temp]
                nums[temp] = temp

    print(duplicated_list)

'''
slow and fast pointer, like question circle in a linkedlist
'''
def solution4(nums):
    slow = nums[0]
    fast = nums[nums[0]]


    while nums[slow] != nums[fast]:
        slow = nums[slow]
        fast = nums[nums[fast]]

    head = 0
    while nums[slow] != nums[head]:
        slow = nums[slow]
        head = nums[head]

    return nums[head]


if __name__ == '__main__':
    array = list(np.random.choice(list(range(20)), 20))
    solution3(array)

    cases = [[1,3,4,2,2], [3,1,3,4,2], [1,1,2,3,4]]
    for case in cases:
        print(solution4(case))