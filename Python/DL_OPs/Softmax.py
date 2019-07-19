import numpy as np

class Softmax(object):
    def __init__(self):
        pass

    def forward(self, x):
        self.out = x
        self.out -= np.max(self.out)
        self.out = np.exp(self.out)
        denominator = sum(self.out)
        self.out /= denominator

        return self.out

    def backprop(self, eta):
        dout = np.diag(self.out) - np.dot(self.out, self.out.T)
        return np.dot(dout, eta)


if __name__ == '__main__':
    softmax = Softmax()
    tensor = [1, 2, 3, 4]
    print(softmax.forward(tensor))
    eta = [0.3, 0.55, 0.34, 0.44]
    print(softmax.backprop(eta))
