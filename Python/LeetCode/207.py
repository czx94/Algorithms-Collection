class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(i):
            if status[i] == -1:
                return False
            elif status[i] == 1:
                return True

            status[i] = -1
            for j in afterward[i]:
                if not dfs(j):
                    return False

            status[i] = 1
            return True

        status = [0]*numCourses
        afterward = [[] for _ in range(numCourses)]

        for c, after in prerequisites:
            afterward[c].append(after)

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True