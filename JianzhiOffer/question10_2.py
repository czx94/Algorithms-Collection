# Recursive one, stupid
def solution1(n):
    assert n > 0
    if n == 1:
       return 1
    elif n == 2:
        return 2
    else:
        return solution1(n - 1) + solution1(n - 2)

# iterative
def solution2(n):
    assert n > 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        prev_prev = 1
        prev = 2
        for _ in range(2, n):
            prev, prev_prev = prev_prev + prev, prev

        return prev

if __name__ == '__main__':
    number = solution1(3)
    print(number)
    number = solution2(3)
    print(number)