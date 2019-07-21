//
// Created by caizixiang on 2019-07-20.
//
using namespace std;
#include <unordered_map>

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

int main() {
    Solution two_sum;
    vector<vector<int>> cases = [[2, 7, 11, 15], [0, 2, 4, 9]];
    vector<int> targets = [9, 11];

}
