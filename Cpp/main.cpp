//
// Created by caizixiang on 2019-07-19.
//
using namespace::std;
#include <iostream>
#include <vector>

int main() {
    string s = "hello world";
    for (auto it = s.begin(); it != s.end() && !isspace(*it); ++it)
    {
        *it = toupper(*it);
    }
    for (auto ch: s)
        cout << ch << endl;
    return 0;
}