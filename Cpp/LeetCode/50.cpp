//
// Created by caizixiang on 2019-07-20.
//

class Solution {
public:
    double myPow(double x, int n) {
        if (x == 1)
            return x;

        if (n < 0)
        {
            if (n == INT_MIN)
            {
                return 1 / x * myPow(x, n + 1);
            }
            return 1 / myPow(x, -n);
        }

        if (n == 0)
            return 1;
        else if (n == 1)
            return x;
        else
        if (n & 1)
            return x*myPow(x*x, n>>1);
        else
            return myPow(x*x, n>>1);

    }
};
