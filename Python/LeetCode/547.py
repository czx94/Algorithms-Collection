'''
There are N students in a class.
Some of them are friends, while some are not.
Their friendship is transitive in nature.
For example, if A is a direct friend of B,
and B is a direct friend of C,
then A is an indirect friend of C.
 And we defined a friend circle is a group of students
 who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other,
otherwise not. And you have to output the total number of friend circles among all the students.
'''

class Solution(object):
    # union set
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def find(root):
            while roots[root] != root:
                root = roots[root]

            return root

        if len(M) < 2:
            return len(M)

        roots = list(range(len(M)))
        for i in range(len(M)):
            for j in range(i+1, len(M)):
                if M[i][j] == 1:
                    index_j = find(j)
                    index_i = find(i)
                    if index_i > index_j:
                        roots[index_i] = index_j
                    else:
                        roots[index_j] = index_i

        for i in range(len(M)):
            while roots[i] != roots[roots[i]]:
                roots[i] = roots[roots[i]]

        result = {}
        for root in roots:
            result[root] = result.get(root, 0) + 1

        return len(result.values())

if __name__ == '__main__':
    cases = [
            [[1,1,0],
             [1,1,0],
             [0,0,1]],
            [[1, 1, 0],
             [1, 1, 1],
             [0, 1, 1]],
            [[1, 0, 0, 1],
             [0, 1, 1, 0],
             [0, 1, 1, 1],
             [1, 0, 1, 1]],
        [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         ],
        [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]
             ]
    solution = Solution()
    for case in cases:
        print(solution.findCircleNum(case))