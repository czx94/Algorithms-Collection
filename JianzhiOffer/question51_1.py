'''
reverse pairs
leetcode493
'''

def solution1(nums):
    if not nums:
        return

    def merge_helper(left, right):
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                l += 1
            else:
                nonlocal count
                count += len(left) - l
                r += 1
        return merge(left, right)

    def sort(lst):
        if len(lst) <= 1:
            return lst
        else:
            return merge_helper(sort(lst[:len(lst)//2]), sort(lst[len(lst)//2:]))

    def merge(left, right):
        merged_list = list()

        while left and right:
            if left[0] < right[0]:
                value = left.pop(0)
            else:
                value = right.pop(0)

            merged_list.append(value)

        if left:
            merged_list += left
        else:
            merged_list += right

        return merged_list

    count = 0
    sort(nums)
    return count



if __name__ == '__main__':
    nums = [7, 5, 6, 4]
    result = solution1(nums)
    print(result)

