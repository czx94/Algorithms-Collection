'''
find the first element non-repeated
leetcode 387
'''

def solution1(string):
    count_dict = dict()

    for s in string:
        if s not in count_dict:
            count_dict[s] = 1
        else:
            count_dict[s] += 1

    for s in string:
        if count_dict[s] == 1:
            return s

if __name__ == '__main__':
    string = 'abaccdeff'
    result = solution1(string)
    print(result)