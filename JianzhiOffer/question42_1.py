'''
The maximum sum of a continuous subset
'''

# this solution is good for sum > 0, but cannot deal with the case sum < 0
def solution1(input_list):
    max_sum = 0
    current_sum = 0
    for element in input_list:
        current_sum = max(current_sum + element, 0)
        max_sum = max(current_sum, max_sum)

    return max_sum

# ac, but too slow
def solution2(nums):
    if not nums:
        return None

    max_sum = nums[0]
    element_list = []
    for num in nums:
        element_list.append(num)
        current_sum = sum(element_list)
        if current_sum < 0:
            element_list = []
        max_sum = max(current_sum, max_sum)

    return max_sum

# faster
def solution3(nums):
    if not nums:
        return None

    current_sum = 0
    max_sum = nums[0]
    element_list = []

    for num in nums:
        element_list.append(num)
        current_sum += num
        max_sum = max(current_sum, max_sum)

        if current_sum < 0:
            element_list = []
            current_sum = 0

    return max_sum

if __name__ == '__main__':
    cases = [([1, -2, 3, 10, -4, 7, 2, -5], 18)]
    for case in cases:
        print(case)
        print(solution1(case[0]))
    for case in cases:
        print(case)
        print(solution2(case[0]))
    for case in cases:
        print(case)
        print(solution3(case[0]))