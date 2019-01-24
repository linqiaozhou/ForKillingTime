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
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [âˆ’231,  231 âˆ’ 1]. 
For the purpose of this problem, assume that your function returns 231 âˆ’ 1 when the division result overflows.*/
#include"common.hpp"
class Solution {
public:
    int divide(int dividend, int divisor) {
        
         if (dividend == INT_MIN && divisor == -1)
            return INT_MAX;
         if (dividend == 0 || divisor == 0)
            return 0;

        int nega = 0;
        if ((dividend>0&&divisor<0) || (dividend<0&&divisor>0))
            nega = 1;
        long long d=dividend;//intÊı¾İabs(-2147483648)»áÒç³ö£¬ÒòÎªÕıÊıintÖ»ÄÜµ½2147483647,ËùÒÔĞèÒªlong long À´´æ´¢Ò»ÏÂ
        long long s=divisor;
        long long den = abs(d);
        long long sor = abs(s);
        if (sor > den)
            return 0;
        long long sum = 0;
        int count = 0;
        int res = 0;
        while (den >= sor)
        {
            count = 1;                //a >= b±£Ö¤ÁË×îÉÙÓĞÒ»¸öcount
            sum = sor;
            while (sum + sum <= den){    //!!
                sum += sum;
                count += count;
            }
            den -= sum;
            res += count;
        }

        if (nega)
            res = 0 - res;
        return res;
    }
};
