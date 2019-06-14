'''
Concat a list of number into a smallest number
'''
import numpy as np

# sort it
def solution1(nums, k):
    if not nums:
        return

    return sorted(nums)[:k]

def solution2(nums, k):
    if not nums:
        return




if __name__ == '__main__':
    element_list = list(np.random.choice(100, size=20, replace=False))
    k = 5
    print(element_list, k)
    result = solution1(element_list, k)
    print(result)