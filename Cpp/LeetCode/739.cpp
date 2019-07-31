//
// Created by caizixiang on 2019-07-30.
//

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> result(T.size(), 0);
        vector<int> stack;

        for (int i = 0; i < T.size(); i++)
        {
            while (!stack.empty() && T[stack.back()] < T[i])
            {
                int index = stack.back();
                stack.pop_back();
                result[index] = i - index;
            }
            stack.push_back(i);
        }

        return result;
    }
};