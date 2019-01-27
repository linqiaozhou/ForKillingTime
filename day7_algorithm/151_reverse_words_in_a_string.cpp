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
    void swap(char& a,char& b)
    {
        char temp = a;
        a=b;
        b=temp;
    }
    void reverseStr(string&s, int start, int end)
    {
        while(start<end)
        {
            swap(s[start],s[end]);
            start++;
            end--;
        }
    }
    void reverseWords(string &s) {
    	int len = s.size();
        int start = 0;
        int end = len - 1;
        
        reverseStr(s, start, end);

        start = 0;
        end = start;   
        //process leading spaces
        while(end != len && s[end] == ' ')
        {
    	    end++;
        }
        int space_num = end - start;
        if(space_num > 0)
        {
        	len -= space_num; 
        	for(int i = 0; i < len; i++)
        	{
        		s[start+i] = s[end + i];
        	}
        }

        //while(s[start]!='\0')
        while(start != len)
        {	
        	while(start != len && s[start] != ' ')
        	{
        		start++;
        	}
        	if(start == len) break;
            end = start;  
            while(end != len && s[end] == ' ')
        	{
        		end++;
        	}
        	space_num = end - start;
        	//process trailing spaces
        	if(end == len && space_num > 0)
			{
				for(int i = 0; i < space_num; i++)
				{
					s[start+i] = s[end+i];
				}
				len -= space_num; 
				break;
			}
			else if(space_num > 1)
			{
			    len = len - space_num + 1;
				
				for(int i = 0; i < len; i++)
				{
					s[start + 1 +i] = s[end+i];
				}
			}
			start++;
        }
        s.resize(len);
        //reverse the word
        start = 0;
        end = start;
        while(start != len)
        {
            while(end != len && s[end] != ' ')
            {
                end++;
            }
            if(end == len)
            {
            	reverseStr(s,start,end-1);
            	break;
            }
            reverseStr(s,start,end-1);
            end++;
            start = end;
        }
    }
};