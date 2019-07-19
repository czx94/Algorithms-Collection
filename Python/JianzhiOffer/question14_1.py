'''
Seperate a number into several, maximize their product
'''

# recursive
def solution1(n):
    if n <= 4:
        return n
    else:
        return max(map(lambda x: solution1(x)*solution1(n-x), range(1, n//2 + 1)))

# dp
def solution2(n):
    result_list = [1,2]

    for i in range(3, n+1):
        max_mult = max(list(map(lambda x: result_list[x] * (i-x-1), range(i-1))))
        result_list.append(max_mult)
        print(result_list, i)

    return max_mult

if __name__ == '__main__':
    result = solution1(8)
    print(result)
    result = solution2(8)
    print(result)