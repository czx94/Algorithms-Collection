'''
Count the Card of a given number in a sorted list
'''

# can't solve 1 element list
def solution1(nums, k):
    def get_first_k(nums, k):
        head = 0
        tail = len(nums) - 1
        while head < tail:
            mid = (head + tail) // 2
            if nums[mid] == k:
                if nums[mid-1] != k:
                    return mid
                else:
                    tail = mid
            elif nums[mid] < k:
                head = mid + 1
            else:
                tail = mid - 1

        return head

    def get_last_k(nums, k):
        head = 0
        tail = len(nums) - 1
        while head < tail:
            mid = (head + tail) // 2
            if nums[mid] == k:
                if nums[mid+1] != k:
                    return mid
                else:
                    head = mid
            elif nums[mid] <= k:
                head = mid + 1
            else:
                tail = mid - 1

        return tail

    last_index = get_last_k(nums, k)
    first_index = get_first_k(nums, k)

    return last_index - first_index + 1 if last_index >= first_index else 0

# solve all the cases
def solution2(nums, k):
    def get_first_k(nums, k):
        head, tail = 0, len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if k > nums[mid]:
                head = mid + 1
            else:
                tail = mid - 1
        return head

    def get_last_k(nums, k):
        head, tail = 0, len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if k >= nums[mid]:
                head = mid + 1
            else:
                tail = mid - 1
        return tail

    last_index = get_last_k(nums, k)
    first_index = get_first_k(nums, k)

    return last_index - first_index + 1 if last_index >= first_index else 0

if __name__ == '__main__':
    nums = [1, 2, 3, 3, 3, 3, 4, 5]
    result = solution2(nums, 3)
    print(result)
    nums = [5, 7, 7, 8, 8, 10]
    result = solution2(nums, 6)
    print(result)
    nums = [1]
    result = solution2(nums, 1)
    print(result)