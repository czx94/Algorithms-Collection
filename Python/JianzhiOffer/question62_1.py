'''
Joseph Problem
leetcode 292
'''

def solution1(n, m):
    if n < 1 or m < 1:
        return -1

    nums = list(range(n))

    index = 0
    while True:
        if len(nums) == 1:
            return nums.pop()

        count = 0
        while count < m-1:
            if index < len(nums) - 1:
                index += 1
            else:
                index = 0
            count += 1

        nums.pop(index)
        if index == len(nums):
            index = 0

# math solution
def solution2(n, m):
    if n < 1 or m < 1:
        return -1

    last = 0
    for i in range(2, n+1):
        last = (last + m) % i

    return last


if __name__ == '__main__':
    result = solution1(5, 3)
    print(result)
    result = solution2(5, 3)
    print(result)
