//
// Created by caizixiang on 2019-08-02.
//

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        auto cmp = [](const vector<int> &a, const vector<int> &b)
        {
            return a[0] > b[0] || (a[0] == b[0] && a[1] < b[1]);
        };

        sort(people.begin(), people.end(), cmp);

        vector<vector<int>> result;
        for (int i = 0; i < people.size(); i++) {
            result.insert(result.begin() + people[i][1], people[i]);
        }
        return result;
    }
};