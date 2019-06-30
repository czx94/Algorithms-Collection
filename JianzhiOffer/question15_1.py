'''
Count the one's in the binary representation of a given number
leetcode 191
'''

# works only for positive number
def solution1(number):
    count = 0
    while number:
        if number & 1:
            count += 1
        number >>= 1
    return count

# slow
def solution2(number):
    count = 0
    flag = 1
    while flag <= number:
        if number & flag:
            count += 1
        flag <<= 1
    return count

# magical solution
def solution3(number):
    count = 0
    while number:
        count += 1
        number &= number - 1
    return count


if __name__ == '__main__':
    number = 111
    print(solution1(number))
    print(solution2(number))
    print(solution3(number))