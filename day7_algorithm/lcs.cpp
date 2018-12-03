#include <string>
#include <iostream>

using namespace std;

static int get_longest_common_str(string str1, string str2)
{
    int len1 = str1.size();
    int len2 = str2.size();
    int mat[len1+1][len2+1];
    int max  = 0;
    for(int i = 0; i <= len1; i++)
        for(int j = 0; j <= len2; j++)
        {
            if(i == 0 || j == 0)
            {
                mat[i][j] = 0;
                continue;
            }
            mat[i][j] = (str1[i-1] == str2[j - 1])?\
                       mat[i-1][j-1] + 1: 0;
            if(mat[i][j]>max) max = mat[i][j];
        }
    return max;
}

static void test_lcs1()
{
    string str1 = "linqiaozhou";
    string str2 = "I am linqiaozhou";
    int max = get_longest_common_str(str1,str2);
    if(max==11) 
    {
        cout<<"correct"<<endl;
    }
    else
    {
         cout<<"wrong!the real value is : "<<11<<", the ret is :"<< max <<endl;
    }
}

int main(int argc, char** argv)
{
    test_lcs1();
    return 0;
}
