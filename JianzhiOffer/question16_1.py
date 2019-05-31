'''
Power function
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
        return 1 / non_negative_power(base, exponent)
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
        return 1 / non_negative_power(base, exponent)
    else:
        return non_negative_power(base, exponent)

if __name__ == '__main__':
    base = 2
    exponent = 5
    result = solution1(base, exponent)
    print(result)
    result = solution2(base, exponent)
    print(result)