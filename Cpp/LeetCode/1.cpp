//
// Created by caizixiang on 2019-07-20.
//
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mem;
        vector<int> result;

        for (int i = 0; i < nums.size(); ++i)
        {
            if(mem.count(nums[i]))
            {
                result.push_back(i);
                result.push_back(mem[nums[i]]);
                break;
            }
            mem[target-nums[i]] = i;
        }

        return result;
    }
};

