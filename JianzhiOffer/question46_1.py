'''
Translate a number into string, calculate how many combinations are there
'''

translate_table = {}
for i in range(26):
    translate_table[i] = chr(ord('a')+i)
print(translate_table)

def solution1(num):
    if num < 0:
        num = -num
        
    def recursive(num):
        if len(num) <= 1:
            return 1
        else:
            if int(num[:2]) in translate_table:
                return recursive(num[2:]) + recursive(num[1:])
            else:
                return recursive(num[1:])

    return recursive(str(num))


if __name__ == '__main__':
    num = 122582625
    result = solution1(num)
    print(result)