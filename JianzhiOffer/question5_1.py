'''
Replace the 'spaces' in a given string

lintcode 212
'''
def solution1(string):
    string = string.replace(' ', '%20')
    return string


if __name__ == '__main__':
    string = 'We are happy'
    result = solution1(string)
    print(result)