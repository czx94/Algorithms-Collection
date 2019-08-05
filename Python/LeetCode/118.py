'''
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []

        result = [[1]]
        if numRows > 1:
            for i in range(1, numRows):
                result.append([1] + list(map(lambda x: x[0]+x[1], zip(result[-1], result[-1][1:] + [0]))))
                
        return result
    
    
if __name__ == '__main__':
    cases = [1, 3, 5]
    solution = Solution()
    for case in cases:
        print(solution.generate(case))
        
                
                

