'''
Translate a number into string, calculate how many combinations are there
leetcode 17
acwing 59
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

# acwing 59
class Solution:
    def getTranslationCount(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 1

        else:
            if int(s[:2]) <= 25 and int(s[0]) != 0:
                return (self.getTranslationCount(s[2:]) + self.getTranslationCount(s[1:]))
            else:
                return self.getTranslationCount(s[1:])

if __name__ == '__main__':
    num = 122582625
    result = solution1(num)
    print(result)