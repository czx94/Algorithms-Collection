class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l1, l2 = len(nums1), len(nums2)

        # i + j = l1 - i + l2 - j => j = (l1 + l2)//2 -i
        # l1 <= l2 => j > 0
        # search m
        head = 0
        tail = l1
        half_len = (l1+l2+1) >> 1
        while head <= tail:
            i = (head+tail) >> 1
            j = half_len - i
            if i > 0 and nums1[i-1] > nums2[j]:
                tail = i - 1
            elif i < l1 and nums1[i] < nums2[j-1]:
                head = i + 1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (l1 + l2) & 1:
                    return max_of_left

                if i == l1:
                    min_of_right = nums2[j]
                elif j == l2:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2


        # while head <= tail:
        #     i = (head+tail) >> 1
        #     j = half_len - i
        #     print(i, j)
        #     if nums1[i-1] < nums2[j] and nums1[i] > nums2[j-1]:
        #         break
        #     elif nums1[i-1] > nums2[j]:
        #         tail = i - 1
        #     elif nums1[i] < nums2[j-1]:
        #         head = i + 1
        #
        # if (l1 + l2) & 1:
        #     return max(nums1[i-1], nums2[j-1])
        # else:
        #     return (max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j]))/2

if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(nums1, nums2)
    print(solution.findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(nums1, nums2)
    print(solution.findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 2, 3]
    nums2 = [4, 5 ,6, 7, 8, 9]
    print(nums1, nums2)
    print(solution.findMedianSortedArrays(nums1, nums2))
