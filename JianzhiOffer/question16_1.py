'''
Power function
leetcode 50
'''

# naive
def solution1(base, exponent):
    def non_negative_power(base, exponent):
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        else:
            res = 1
            for _ in range(exponent):
                res *= base
            return res

    if base == 0:
        return 0

    if exponent < 0:
        return 1 / non_negative_power(base, -exponent)
    else:
        return non_negative_power(base, exponent)

# faster
def solution2(base, exponent):
    def non_negative_power(base, exponent):
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        else:
            res = non_negative_power(base, exponent>>1)
            res *= res
            if exponent & 1 == 1:
                res *= base
            return res

    if base == 0:
        return 0

    if exponent < 0:
        return 1 / non_negative_power(base, -exponent)
    else:
        return non_negative_power(base, exponent)

# like 2 but clearer
def solution3(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        res = 1/solution3(base, -exponent)
        return res
    else:
        if exponent & 1 == 0:
            return solution3(base*base, exponent>>1)
        else:
            return base*solution3(base, exponent-1)

if __name__ == '__main__':
    base = 2
    exponent = -2
    result = solution1(base, exponent)
    print(result)
    result = solution2(base, exponent)
    print(result)
    result = solution3(base, exponent)
    print(result)