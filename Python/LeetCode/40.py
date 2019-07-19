class Solution(object):
    def combinationSum2_1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # first sort the numbers
        candidates.sort()
        result = list()
        self.recursive_search(target, [], 0, result, candidates)
        return result

    def recursive_search(self, target, current_result, start, result, candidates):
        if not target:
            result.append(current_result)

        for i in range(start, len(candidates)):
            if i > start and candidates[i - 1] == candidates[i]:
                continue

            if candidates[i] > target:
                break

            self.recursive_search(target-candidates[i], current_result+[candidates[i]], i+1, result, candidates)

    def combinationSum2_2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [set() for _ in range(target + 1)]
        dp[0].add(())
        for num in candidates:
            for t in range(target, num - 1, -1):
                print(num, dp)
                for prev in dp[t - num]:
                    dp[t].add(prev + (num,))

        for d in dp:print(d)
        return list(dp[-1])

if __name__ == '__main__':
    solution = Solution()
    cases = [([10,1,2,7,6,1,5], 8)]
    for case in cases:
        print('######')
        print('input:',case)
        print('output:',solution.combinationSum2_1(case[0], case[1]))
        print('output:',solution.combinationSum2_2(case[0], case[1]))
        print('######')