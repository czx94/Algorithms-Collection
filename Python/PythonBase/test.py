# question1
print('question1')
row = [""]*2
board = [row]*2
board[0][0] = "X"
print(board)

'''
A. [['X', ''], ['', '']]
B. [['X', ''], ['X', '']]
C. [['', ''], ['X', '']]
D. [['', ''], ['', '']]
B
'''

# question2
print('question2')
some_tuple = ("A", "tuple", "with", "values")
another_tuple = ([1, 2], [3, 4], [5, 6])
# some_tuple[2] = "change this" # 1
# another_tuple[2].append(1000) # 2
# another_tuple[2] += [99, 999] # 3

'''
# 下面三句话中，能够正常运行的有？
some_tuple[2] = "change this" # 1
another_tuple[2].append(1000) # 2
another_tuple[2] += [99, 999] # 3
A. 1, 2, 3
B. 2, 3
C. 都会报错
D. 2
D
'''

# question3
# print('question3')
# a = 1
# def some_func():
#     return a
#
# def another_func():
#     a += 1
#     return a
#
# print(some_func())
# print(another_func())

'''
下面这段代码中，两次函数调用的输出依次是？
A. 1 2
B. 1 UnboundLocalError
C. UnboundLocalError UnboundLocalError
D. UnboundLocalError 2
'''

# question4
print('question4')
x, y = (0, 1) if True else None, None
print(x, y)

'''
请写出下面这段代码对应的输出？
(0, 1) None
'''

# question5
print('question5')
# 如何用列表推导(list comprehension)来简化下述代码到一行？
l = []
for i in range(100):
    l.append(i)

# l = [i for i in range(100)]


# question6
print('question6')

'''Python中import下面哪个库会打印Python之禅？
A. import antigravity
B. import this
C. import __future__
D. import zen
B
'''

# question7
'''
列举出你知道的Python中以双下划线开头和结尾的魔法函数，并指出其作用。
列举三个即可。
'''
#__init__: 类的初始化函数
class Exemple1():
    def __init__(self, nothing):
        self.nothing = nothing

exemple1 = Exemple1('nothing')

#__call__: 使得类的实例具有函数的特性
class Exemple2():
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('test')

exemple2 = Exemple2()
exemple2()

#__len__: 使得类的实例可以被len度量
class Exemple3():
    def __init__(self, nums):
        self.nums = nums

    def __len__(self):
        return self.nums[-1]

exemple3 = Exemple3([1, 2, 3])
print(len(exemple3))

#__getitem__: 使得类的实例具有可迭代性
class Exemple4():
    def __init__(self, nums):
        self.nums = nums

    def __getitem__(self, item):
        return self.nums[item]

exemple4 = Exemple4([4, 2, 6, 7])
for num in exemple4:
    print(num)

#__str__: 格式化字符串
#__repr__: 目的是为了表示清楚，是为开发者准备的
#__str__ 方法默认调用了__repr__方法
class Exemple5:
    def __init__(self,text):
        self.text = text

    def __repr__(self):
        return (self.text + '\n')*3

exemple5 = Exemple5('test')
print(str(exemple5))
print(repr(exemple5))

import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today))
# Reference: http://www.langzi.fun/Python%E9%AD%94%E6%B3%95%E5%87%BD%E6%95%B0.html


#__enter__, __exit__, with所求值的对象必须有一个enter()方法和一个exit()方法
#with开始，先执行enter方法，退出时执行exit方法
#https://www.jianshu.com/p/c39a523f7142
class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print("In__exit__()")

def get_sample():
    return Sample()

with get_sample() as sample:
    print(sample)


#__slots__: 用来限制类的属性
class Exemple6():
    __slots__ = ('value', 'elements')

# question8
'''
一句话说明下面使用with包装整个语句块的好处是什么？
with open("file path") as f:
# 进行文件内容处理
# ...

（１）紧跟with后面的语句被求值后，返回对象的__enter__方法被调用，这个方法的返回值将被赋值给as后面的变量；
（２）当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__方法。
对代码的优雅性是有极大帮助，让代码更简练。同时在异常产生时，清理工作更简单。
'''


# question9
'''
下列选项中，能填写在代码的划线空白处，使代码输出100的是？
class A:
    @__________________
    def score(self):
        return 100
a = A()
print(a.score)

A. attribute
B. getter
C. property
D. score.getter
C
'''
print('question9')
class A:
    @property
    def score(self):
        return 100
a = A()
print(a.score)


# question10
'''
Python中哪些库可以用于创建新的进程或线程？
A. multiprocess
B. threading
C. concurrent.futures
D. subprocess
E. os.fork
'''


# question11
'''
Python中对于CPU密集型和IO密集型任务分别采用怎样的方式提速？
A. CPU 密集：多进程 or 多线程；IO 密集：多进程 or 多线程
B. CPU 密集：多进程；IO 密集：多进程 or 多线程
C. CPU 密集：多进程； IO 密集：多线程
D. CPU 密集：多线程；IO 密集：多进程
'''


# question12
'''
请问下述代码中的，单下划线的作用是？
for _ in range(100):
    print("-", end="")
def func():
    return 1, 2
_, b = func()

接收一个变量
'''


# question13
'''
下面这段代码的输出是？
A. Java Ruby Javascript Python
B. Python Ruby Python Python
C. Java Ruby Python Python
D. Python Ruby Javascript Python
C
'''

print('question13')
some_dict = {}
some_dict[True] = "Java"
some_dict[1.5] = "Ruby"
some_dict[1.0] = "JavaScript"
some_dict[1] = "Python"
print(some_dict[True], some_dict[1.5], some_dict[1.0], some_dict[1])


# question14
'''
请写出下面这段代码的输出？
0 1 2
'''

print('question14')
for i in range(3):
    print(i)
    i = 5


# question15
'''
请写出下面这段代码的输出？
[1, 2, 3, 4]
[2, 4]
[]
[2, 4]
'''

print('question15')
list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]
for idx, item in enumerate(list_1):
    del item
for idx, item in enumerate(list_2):
    list_2.remove(item)
for idx, item in enumerate(list_3[:]):
    list_3.remove(item)
for idx, item in enumerate(list_4):
    list_4.pop(idx)
print(list_1)
print(list_2)
print(list_3)
print(list_4)


# question16
'''
以下代码块的输出结果是什么？
A. [1, [2, 3]]
B. [1, [2, 5]]
C. [4, [2, 3]]
D. [4, [2, 5]]
B
'''

print('question16')
l1 = [1, [2, 3]]
l2 = list(l1)
l3 = l1[:]
l2[0] = 4
l2[1][1] = 5
print(l3)


# question17
'''
以下代码块的输出是什么？
A. 1 2 1 1 3
B. 1 2 1 2 1 3
C. 1 2 1 3
D. 1 2 1 3 1 2 1 3
'''

print('question17')
def func(arg = []):
    arg.append(1)
    return arg
a = func()
a.append(2)
b = func()
b.append(3)
print(*a, *b)
