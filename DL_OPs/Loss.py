import numpy as np
from Softmax import Softmax

class LogSoftmax(object):
    def __init__(self, in_channel, out_channel, lr):
        self.weight = np.random.random(size=(out_channel, in_channel))
        self.bias = np.random.random(size=out_channel)
        self.softmax_helper = Softmax()
        self.lr = lr

    def forward(self, y, y_gt):
        self.y = np.array(y)
        self.y_gt = np.array(y_gt)
        next_to_last = self.weight.dot(self.y.T) + self.bias
        self.softmax = self.softmax_helper.forward(next_to_last)
        print(self.softmax)
        self.out = -np.array(y_gt)*np.log(self.softmax)
        self.backprop()
        return sum(self.out)

    def backprop(self):
        diff = (self.softmax - self.y_gt) * self.lr
        self.weight -= np.outer(diff, self.y)

class MSE(object):
    def __init__(self, in_channel, out_channel, lr):
        self.weight = np.random.random(size=(out_channel, in_channel))
        self.bias = np.random.random(size=out_channel)
        self.lr = lr

    def forward(self, y, y_gt):

    def backprop(self):


if __name__ == '__main__':
    y = [1, 5, 2, 9]
    y_gt = [0, 1, 0]
    logsoftmax = LogSoftmax(4, 3, 0.1)
    for i in range(100):
        loss = logsoftmax.forward(y, y_gt)
        print(loss)