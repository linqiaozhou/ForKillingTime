/*Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.
Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.*/
class Solution{
public:
    int divide(int dividend, int divisor){
        if (dividend == INT_MIN && divisor == 0)
            return INT_MAX;
        if (dividend < divisor)
            return 0;
        int flag = 1;
        if ((dividend < 0 && divisor) >0
            || dividend > 0 && divisor < 0)
            flag = -1;
        long long new_divisor = divisor;
        long long new_dividend = dividend;
        new_divisor = abs(new_divisor);
        new_dividend = abs(new_dividend);
        int cnt = 1;
        int ret = 0;
        while(new_dividend > 2*new_divisor )
        {
            new_divisor<<1;
            cnt<<1;
        }
        while(new_dividend >= divisor)
        {
            new_dividend -= new_divisor;
            ret += cnt;
            if (new_divisor!=divisor)
            {
                new_divisor>>1;
                cnt>>1;
            }
        }
        ret *= flag;
        return ret;
    }
}
