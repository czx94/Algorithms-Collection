'''
Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''


class Solution(object):
    def longestConsecutive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_len = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                max_len = max(max_len, y - x)
                x += 1

        return max_len


    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = dict()
        max_len = 0
        for num in nums:
            if num in record:
                continue
            else:
                record[num] = record.get(num+1, 0) + record.get(num-1, 0) + 1
                if num + 1 in record:
                    record[num+record[num+1]] = record[num]
                if num - 1 in record:
                    record[num-record[num-1]] = record[num]

                max_len = max(max_len, record[num])

        return max_len
    
    
    # union set
    def longestConsecutive3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_root(key):
            while roots[key] != key:
                key = roots[key]

            return key

        def set_root(key1, key2):
            if sizes[key1] > sizes[key2]:
                sizes[key1] += sizes[key2]
                roots[key2] = key1
            else:
                sizes[key2] += sizes[key1]
                roots[key1] = key2

        if len(nums) < 2:
            return len(nums)

        roots = list(range(len(nums)))
        sizes = [1]*len(nums)
        record = dict()
        for i in range(len(nums)):
            if nums[i] in record:
                continue
            record[nums[i]] = i
            if nums[i]-1 in record:
                root = find_root(record[nums[i]-1])
                root_i = find_root(i)
                set_root(root, root_i)
            if nums[i]+1 in record:
                root = find_root(record[nums[i]+1])
                root_i = find_root(i)
                set_root(root, root_i)

        return max(sizes)

if __name__ == '__main__':
    cases = [[100, 4, 200, 1, 3, 2], [3,5,7,9,112,43,42,41,45,34,44], [1,3,5,2,4]]
    solution = Solution()
    for case in cases:
        print(solution.longestConsecutive3(case))
