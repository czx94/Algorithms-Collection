class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0

        volume = 0
        head = 0
        tail = len(height) - 1
        h_max, t_max = height[head], height[tail]
        while head < tail:
            h_max, t_max = max(h_max, height[head]), max(t_max, height[tail])
            if h_max <= t_max:
                volume += h_max - height[head]
                head += 1
            else:
                volume += t_max - height[tail]
                tail -= 1

        return volume