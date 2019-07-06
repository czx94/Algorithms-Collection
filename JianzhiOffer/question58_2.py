'''
Rotate string to the left
'''

def solution(s, k):
    k = k % len(s)
    s = s[k:] + s[:k]
    return s

if __name__ == '__main__':
    print(solution('abcdefg', 2))