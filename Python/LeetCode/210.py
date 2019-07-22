class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        after_courses = [[] for _ in range(numCourses)]
        count = [0] * numCourses
        for after, prev in prerequisites:
            count[after] += 1
            after_courses[prev].append(after)

        result = []
        for i in range(numCourses):
            if count[i] == 0:
                result.append(i)

        index = 0
        while index != len(result):
            last = result[index]
            index += 1
            for num in after_courses[last]:
                count[num] -= 1
                if count[num] == 0:
                    result.append(num)

        return result if index == numCourses else []


