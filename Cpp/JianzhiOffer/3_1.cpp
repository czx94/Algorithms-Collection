//
// Created by caizixiang on 2019-07-27.
//
//Find the repeated numbers in a list
//
//List l has a length of n, all its elements are integers between 0 and n - 1.
//Some of the elements are repeated, but we don't know how many of them are and for how many times
//Objective is to find any of the repeated numbers
//
//leetcode 287

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int solution1(vector<int> nums)
{
    int slow = nums[0];
    int fast = nums[nums[0]];

    while (nums[slow] != nums[fast])
    {
        slow = nums[slow];
        fast = nums[nums[fast]];
    }

    int head = 0;
    while (nums[head] != nums[slow])
    {
        head = nums[head];
        slow = nums[slow];
    }

    return nums[head];
}

int solution2(vector<int> nums)
{
    int tail = nums.size() - 1, head = 0, mid;
    while (head <= tail)
    {
        mid = (head + tail) >> 1;
        int count = 0;
        for (int num: nums)
        {
            if (num <= mid)
                count++;
        }

        if (count>mid)
            tail = mid - 1;
        else
            head = mid + 1;
    }

    return head;

}

int main()
{
    vector<vector<int> > cases;
    // case 1
    int temp1[5] = {1,3,4,2,2};
    vector<int> case1(temp1, temp1+5);
    cases.push_back(case1);
    // case2
    int temp2[25] = {3,1,3,4,2};
    vector<int> case2(temp2, temp2+5);
    cases.push_back(case2);


    for (vector<int> this_case: cases)
    {
        vector<int>::iterator ite = this_case.begin();
        for (; ite != this_case.end(); ite++){
            cout << *ite << "\t";
        }
        cout << endl << solution1(this_case) << endl;
        cout << solution2(this_case) << endl;

    }
    return 0;
}