'''
The longest substring without repeated character
leetcode 3
'''

def solution1(string):
    position_dict = dict()
    max_length = 0
    current_length = 0

    for i in range(len(string)):
        if string[i] not in position_dict:
            current_length += 1
        else:
            distance = i - position_dict[string[i]]
            if current_length < distance:
                current_length += 1
            else:
                current_length = distance
        position_dict[string[i]] = i
        max_length = max(max_length, current_length)

    return max_length

if __name__ == '__main__':
    strings = ['arabcacfr', "abba"]
    for string in strings:
        length = solution1(string)
        print(length)

