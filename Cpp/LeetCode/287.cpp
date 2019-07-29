//
// Created by caizixiang on 2019-07-28.
//

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
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
};