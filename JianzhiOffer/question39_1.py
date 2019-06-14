'''
Print the number n, card(n) > len(list)/2
leetcode 169
'''

# too slow
def solution1(list_to_test):
    return findKthLargest(list_to_test, len(list_to_test)//2+1)

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    flag = nums[-1]
    left = []
    right = []

    for num in nums[:-1]:
        if num > flag:
            right.append(num)
        else:
            left.append(num)

    if len(right) == k - 1:
        return flag
    elif len(right) < k - 1:
        return findKthLargest(left, k-len(right)-1)
    else:
        return findKthLargest(right, k)

# eliminer other numbers
def solution2(list_to_test):
    number = None
    count = 0
    for element in list_to_test:
        if not count:
            number = element
            count = 1
        else:
            if number == element:
                count += 1
            else:
                count -= 1

    return number


if __name__ == '__main__':
    list_to_test = [1,2,3,2,2,2,5,4,2]
    number = solution1(list_to_test)
    print(list_to_test, number)
    number = solution2(list_to_test)
    print(list_to_test, number)