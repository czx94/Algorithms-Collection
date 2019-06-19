'''
construct a func add without +-*/
'''
import random
def solution1(n1, n2):
    while n2:
        sum = n1 ^ n2
        carry = (n1 & n2) << 1
        n1 = sum
        n2 = carry

    return n1

if __name__ == '__main__':
    for i in range(5):
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)
        sum = solution1(n1, n2)
        print(n1, n2, sum)