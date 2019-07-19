'''
Construct an array with mult
'''
import numpy as np
def solution1(list_a):
    if not list_a:
        return list_a

    list_b = []
    list_c = []
    list_d = []

    for i in range(len(list_a)):
        if i == 0:
            list_c.append(1)
            list_d.append(1)

        else:
            list_c.append(list_c[-1]*list_a[i])
            list_d.append(list_d[-1]*list_a[::-1][i])

    for i in range(len(list_a)):
        list_b.append(list_c[i]*(list_d[::-1][i]))

    return list_b

def solution2(list_a):
    if not list_a:
        return list_a

    temp_list = np.zeros(len(list_a))

    temp_list[0] = 1
    for i in range(len(list_a)-1):
        temp_list[i+1] = temp_list[i] * list_a[i+1]

    temp = 1
    for i in range(len(list_a)-2, -1, -1):
        temp *= list_a[i]
        temp_list[i] *= temp

    return temp_list


if __name__ == '__main__':
    element_list = list(np.random.choice(10, size=5, replace=False))
    print('###solution1###')
    list_b = solution1(element_list)
    print(element_list)
    print(list_b)

    print('###solution2###')
    list_b = solution2(element_list)
    print(element_list)
    print(list_b)
