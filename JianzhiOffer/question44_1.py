'''
A series is formed by ordered number from 0, 1 to ..., like 0123456789..., from the n-th digits
LeetCode 400
'''

def solution1(n):
    n -= 1
    digits = 1
    while True:
        first = 10 ** (digits - 1)
        if n < 9 * first * digits:
            return int(str(first + n / digits)[n % digits])
        n -= 9 * first * digits
        digits += 1

if __name__ == '__main__':
    result = solution1(1001)
    print(result)
