import numpy as np

def count_sort(list_object, lower, upper):
    assert len(list_object) >= 1
    count_dict = dict()
    sorted_list = [0] * len(list_object)

    for i in range(lower, upper):
        count_dict[i] = 0

    for value in list_object:
        count_dict[value] += 1

    for i in range(lower+1, upper):
        count_dict[i] += count_dict[i-1]


    for i in range(len(list_object)):
        sorted_list[count_dict[list_object[i]]-1] = list_object[i]
        count_dict[list_object[i]] -= 1

    return sorted_list

if __name__ == '__main__':
    list_object = list(np.random.choice(range(10,20), size=15, replace=True))
    sorted_object = count_sort(list_object, 10, 20)
    print(sorted_object)