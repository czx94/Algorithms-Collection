class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = list()
        self.stack2 = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        if not self.stack2:
            self.stack2.append(x)
        else:
            if self.stack2[-1] > x:
                self.stack2.append(x)
            else:
                self.stack2.append(self.stack2[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.stack2.pop()
        return self.stack1.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack2[-1]