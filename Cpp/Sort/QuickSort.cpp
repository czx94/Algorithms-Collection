//
// Created by caizixiang on 2019-08-01.
//

#include <vector>
#include <iostream>

using namespace std;

void quickSort(vector<int> *, int, int);
int partition(vector<int> &, int, int);

void quickSort(vector<int> *nums, int head, int tail)
{
    if (head < tail)
    {
        int pivot = partition(*nums, head, tail);
        quickSort(nums, head, pivot - 1);
        quickSort(nums, pivot + 1, tail);
    }
}

int partition(vector<int> &nums, int head, int tail)
{
    int pivot = head, flag = nums[tail];
    for (int i = head; i < tail; i++)
    {
        if (nums[i] < flag)
        {
            swap(nums[i], nums[pivot]);
            pivot++;
        }
    }
    swap(nums[pivot], nums[tail]);
    return pivot;
}

int main()
{
    int myArray[6] = {1, 4, 2, 5, 0, 7};
    vector<int> nums(myArray, myArray + 6);
    quickSort(&nums, 0, nums.size() - 1);
    for (int i = 0; i < nums.size(); i++)
    {
        cout << nums[i] << endl;
    }
    return 0;
}