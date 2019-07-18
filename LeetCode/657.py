class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        horizon = 0
        vertical = 0

        for move in moves:
            if move == 'U':
                vertical += 1
            elif move == 'D':
                vertical -= 1
            elif move == 'R':
                horizon += 1
            else:
                horizon -= 1

        return (horizon, vertical) == (0, 0)