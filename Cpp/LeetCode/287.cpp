//
// Created by caizixiang on 2019-07-28.
//

class Solution {
public:
    int findDuplicate1(vector<int>& nums) {
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

    int findDuplicate2(vector<int>& nums) {
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
};