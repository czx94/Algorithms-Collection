class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        items = preorder.split(',')
        if items[-1] != '#':
            return False

        count = 1
        for item in items:
            if count == 0:
                return False

            else:
                if item == '#':
                    count -= 1
                else:
                    count += 1

        return (count == 0)
