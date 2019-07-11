class Solution(object):
    def combinationSum1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.results = []
        self.target = target
        self.dfs1(candidates, 0, [])

        return self.results

    def dfs1(self, candidates, current_sum, current_path):
        if current_sum == self.target:
            self.results.append(current_path)
            return

        if not candidates or current_sum > self.target:
            return

        for i in range(len(candidates)):
            self.dfs1(candidates[i:], current_sum + candidates[i], current_path + [candidates[i]])

    # faster solution
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.results = []
        candidates.sort()
        self.dfs2(candidates, [], target)

        return self.results

    def dfs2(self, candidates, current_path, target):
        if target == 0:
            self.results.append(current_path)
            return

        if not candidates:
            return

        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            self.dfs2(candidates[i:], current_path + [candidates[i]], target - candidates[i])