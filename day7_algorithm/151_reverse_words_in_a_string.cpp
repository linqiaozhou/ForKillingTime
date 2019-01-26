/*Given an input string, reverse the string word by word.
Example:  
Input: "the sky is blue",
Output: "blue is sky the".
Note:
A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
*/

class Solution {
public:
    void swap(int& a,int& b)
    {
        int temp = a;
        a=b;
        b=temp;
    }
    void reverse
    void reverseWords(string &s) {
        int start = 0;
        int end = s.size();
        while(start<end)
        {
            swap(s[start],s[end]);
            start++;
            end--;
        }
        //先考虑没有异常空格情况
        start = 0;
        end = start;
        while(start!='\0')
        {
            while(s[end]!=' '&&s[end]!='\0')
            {
                end++;
            }
            
        }
    }
};
