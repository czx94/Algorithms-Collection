'''
Count the one's in the binary representation of a given n
leetcode 191
'''

# works only for positive n
def solution1(n):
    count = 0
    while n:
        if n & 1:
            count += 1
        n >>= 1
    return count

# slow
def solution2(n):
    count = 0
    flag = 1
    while flag <= n:
        if n & flag:
            count += 1
        flag <<= 1
    return count

# magical solution
def solution3(n):
    count = 0
    while n:
        count += 1
        n &= n - 1
    return count


if __name__ == '__main__':
    n = 111
    print(solution1(n))
    print(solution2(n))
    print(solution3(n))