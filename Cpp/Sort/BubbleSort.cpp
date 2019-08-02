//
// Created by caizixiang on 2019-08-01.
//

#include <vector>
#include <iostream>

using namespace std;

void bubbleSort(vector<int> *);

void bubbleSort(vector<int> *nums)
{
    for (int i = 0; i < nums.size(); i++)
    {
        int j = i;
        while (j > 0 && nums[j] > nums[j-1])
        {
            swap(nums[j], nums[j - 1]);
            j--;
        }
    }
}

int main()
{
    int myArray[6] = {1, 4, 2, 5, 0, 7};
    vector<int> nums(myArray, myArray + 6);
    bubbleSort(&nums);
    for (int i = 0; i < nums.size(); i++)
    {
        cout << nums[i] << endl;
    }
    return 0;
}

