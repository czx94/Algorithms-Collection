from functools import reduce


class Solution:
    # too slow
    def xorQueries0(self, arr, queries):
        res = list()
        for q in queries:
            res.append(reduce(lambda x, y: x ^ y, arr[q[0]: q[1]+1]))

        return res

    def xorQueries1(self, arr, queries):
        pre_xor = list()
        for item in arr:
            if not pre_xor:
                pre_xor.append(item)
            else:
                pre_xor.append(pre_xor[-1] ^ item)

        res = list()
        for q in queries:
            if q[0] == 0:
                res.append(pre_xor[q[1]])
            else:
                res.append(pre_xor[q[1]]^pre_xor[q[0]-1])

        return res



if __name__ == '__main__':
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    solution = Solution()
    print(solution.xorQueries1(arr, queries))