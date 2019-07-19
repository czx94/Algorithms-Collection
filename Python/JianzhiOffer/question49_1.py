'''
Find the ugly numbers
leetcode 263
'''

# straight forward
def solution1(num):
    def is_ugly_number(num):
        if not num:
            return None

        while not num & 1:
            num >>= 1
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5

        return num == 1

    count = 0
    for i in range(num):
        if is_ugly_number(i):
            count += 1

    return count

def solution2(num):
    if not num:
        return None

    base2 = 0
    base3 = 0
    base5 = 0

    ugly_numbers = [1, 2, 3, 4, 5]

    while ugly_numbers[-1] <= num:
        while ugly_numbers[base2] * 2 <= ugly_numbers[-1]:
            base2 += 1

        while ugly_numbers[base3] * 3 <= ugly_numbers[-1]:
            base3 += 1

        while ugly_numbers[base5] * 5 <= ugly_numbers[-1]:
            base5 += 1

        ugly_numbers.append(min(ugly_numbers[base2] * 2,  ugly_numbers[base3] * 3, ugly_numbers[base5] * 5))

    return len(ugly_numbers) - 1


if __name__ == '__main__':
    print(solution1(23))
    print(solution2(23))