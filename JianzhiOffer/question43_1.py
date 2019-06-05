'''
Output how many times 1 appears in number 1 ... to n
'''

# naive solution
def solution1(n, number=1):
    count = 0
    for i in range(1, n+1):
        num = i
        while num:
            remainder = num % 10
            if remainder == number:
                count += 1
            num //= 10

    return count

def solution2(n, number=1):
    count = 0
    tmp = n
    base = 1
    while tmp:
        last = tmp % 10
        tmp = tmp // 10

        # influenced by the left
        count += tmp * base
        if last == number:
            # influence by the right
            count += n % base + 1
        elif last > number:
            # influence by the left
            count += base
        base *= 10
    return count

if __name__ == '__main__':
    n = 1314
    nums = solution1(n)
    print(n, nums)
    nums = solution2(n)
    print(n, nums)
