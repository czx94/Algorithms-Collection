'''
Given a non-empty array of integers, return the k most frequent elements.
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # count the frequency
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        freq = list(freq.items())
        k_elements = self.qsort(freq, k)

        return k_elements


    def qsort(self, freq, k):
        flag = freq[-1][-1]

        left = []
        right = []
        for element in freq[:-1]:
            if element[-1] > flag:
                left.append(element)
            else:
                right.append(element)

        if len(left) == k:
            return [element[0] for element in left]
        elif len(left) == k - 1:
            left += [freq[-1]]
            return [element[0] for element in left]
        elif len(left) > k:
            return self.qsort(left, k)
        else:
            left += [freq[-1]]
            return [element[0] for element in left] + self.qsort(right, k - len(left))

if __name__ == '__main__':
    solution = Solution()
    cases = [([1,1,1,2,2,3], 2), ([1], 1), ([1, 2], 2), ([4,1,-1,2,-1,2,3], 2), ([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6],10)]
    for case in cases:
        print(solution.topKFrequent(*case))

