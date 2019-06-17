'''
https://www.acwing.com/problem/content/72/
'''

def solution1(target):
    results = []
    small = 1
    big = 2
    current_sum = 3
    current_list = [1, 2]
    if target >= 3:
        while small < big and small <= (target >> 1):
            if current_sum == target:
                results.append(current_list.copy())
                current_sum -= small
                small += 1
                big += 1
                current_sum += big
                current_list.pop(0)
                current_list.append(big)

            elif current_sum < target:
                big += 1
                current_sum += big
                current_list.append(big)

            else:
                current_sum -= small
                small += 1
                current_list.pop(0)

    return results

if __name__ == '__main__':
    result = solution1(15)
    print(result)