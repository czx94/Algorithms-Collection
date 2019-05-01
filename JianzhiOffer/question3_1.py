'''
Find the repeated numbers in a list

List l has a length of n, all its elements are integers between 0 and n - 1.
Some of the elements are repeated, but we don't know how many of them are and for how many times
Objective is to find any of the repeated numbers
'''
import numpy as np

'''
using hashtable to record the frequence of each element
time complexity O(n), space complexity O(n)
'''
def solution1(array):
    hash_table = dict()
    for element in array:
        if element not in hash_table:
            hash_table[element] = 1
        else:
            hash_table[element] += 1

    for key, value in hash_table.items():
        if value > 1:
            print(key, value)

'''
sort the array, then find the repeat ones
time complexity O(nlgn), space complexity O(1)
'''
def solution2(array):
    array = sorted(array)
    index = 0

    print(array)
    while index < len(array) - 1:
        if array[index] == array[index+1]:
            print(array[index])
            while index < len(array) - 1 and array[index] == array[index+1]:
                index += 1

        index += 1


'''
exchange each element with the element in the index of its value
'''
def solution3(array):
    print(array)
    duplicated_list = list()
    for index in range(len(array)):
        while array[index] != index:
            if array[index] == array[array[index]]:
                if array[index] not in duplicated_list: duplicated_list.append(array[index])
                break
            else:
                temp = array[index]
                array[index] = array[temp]
                array[temp] = temp

    print(duplicated_list)

if __name__ == '__main__':
    array = list(np.random.choice(list(range(20)), 20))
    solution3(array)