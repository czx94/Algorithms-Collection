import numpy as np

class conv2d(object):
    def __init__(self, in_channel, out_channel, size, stride, padding):
        self.in_channel = in_channel
        self.out_channel = out_channel
        self.size = size
        self.stride = stride
        self.padding = padding

    def forward(self):
        pass

    def backprop(self):
        pass

class fc(object):
    def __init__(self, in_channel, out_channel):
        self.weight = np.random.random((out_channel, in_channel))
        self.bias = np.random.random(out_channel)