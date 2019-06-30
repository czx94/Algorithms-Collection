'''
Fibonacci
leetcode 509
'''

# recursive solution: not efficient
def solutuion1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return solutuion1(n-1) + solutuion1(n-2)

# iterative solution
def solution2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev_prev = 0
        prev = 1
        for i in range(1, n):
            prev, prev_prev = prev + prev_prev, prev

    return prev

if __name__ == '__main__':
    fibonacci_number = solutuion1(4)
    print(fibonacci_number)
    fibonacci_number = solution2(4)
    print(fibonacci_number)