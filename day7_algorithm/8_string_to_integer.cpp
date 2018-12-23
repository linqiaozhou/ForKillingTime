#include<string>
#include<limits.h>
using namespace std;
class Solution{
public:
    bool isDigit(char c){
       return c>='0'&&c<='9';
    }
    int myAtoi(string str){
        int pos = 0;
        long long ret = 0;
        int len = str.size();
        int flag = 1;
        while(pos < len && str[pos] == ' ')
        {
           ++pos;
        }
        if(pos >= len) return 0;
        if(str[pos] == '-')
        {
            flag = -1;
            ++pos;
        }
        else if(str[pos] == '+')
        {
            ++pos;
        }
        if(pos == len) return 0;
        while(pos < len && isDigit(str[pos]))
        {
           ret *= 10;
           ret += str[pos] - '0';
           long long temp_ret = flag*ret;
           if(temp_ret > INT_MAX)
           {
               return INT_MAX;
           }
           else if(temp_ret < INT_MIN)
           {
               return INT_MIN;
           }
           ++pos;
        }
        return flag*ret;
         
    }
};
