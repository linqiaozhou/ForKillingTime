/*Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", 
it is the fifth second-level revision of the second first-level revision.
You may assume the default revision number for each level of a version number to be 0. 
For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. 
Its third and fourth level revision number are both 0.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
Example 4:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both ¡°01¡± and ¡°001" represent the same number ¡°1¡±
Example 5:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number,
which means its third level revision number is default to "0"
 

Note:

Version strings are composed of numeric strings separated by dots . and this numeric strings may have leading zeroes.
Version strings do not start or end with dots, and they will not be two consecutive dots.
*/

#include"common.hpp" 

class Solution {
public:
	int str2int(const string & str)
	{
		int len = str.size();
		int ret = 0;
		int pos = 0;
		while(str[pos] == '0' && pos < len) 
		{
			if(str[pos] == '0') pos++;
		}
		while(pos < len)
		{
			ret = 10* ret + str[pos] - '0';
			pos++;
		}
		return ret;
	}
	void str2stk(const string& ver, stack<int>& stk, int len)
	{
		int pos  = 0;
        while(pos < len)
        {
        	string sub_ver;
        	while(pos < len && ver[pos] != '.')
        	{
        		sub_ver += ver[pos];
        		pos++;
        	}
        	int sub_ver_num = str2int(sub_ver);
			stk.push(sub_ver_num);   	
        	pos++;
        }
        return;
	}
    int compareVersion(string version1, string version2) {
    	//reverse(version1.begin(), version1.end());
		//reverse(version2.begin(), version2.end()); 
	    int len1 = version1.size();
	    int len2 = version2.size();  
	    stack<int> stk_ver1;
	    stack<int> stk_ver2;
	    str2stk(version1, stk_ver1, len1);
	    str2stk(version2, stk_ver2, len2);
	    
	    stack<int> rev_stk_ver1;
	    stack<int> rev_stk_ver2;
	    
	    
	    while(!stk_ver1.empty())
	    {
	    	rev_stk_ver1.push(stk_ver1.top());
	    	stk_ver1.pop();
	    }
	    
		while(!stk_ver2.empty())
	    {
	    	rev_stk_ver2.push(stk_ver2.top());
	    	stk_ver2.pop();
	    }
	    while(!rev_stk_ver1.empty() && !rev_stk_ver2.empty())
	    {
	        if(rev_stk_ver1.top() > rev_stk_ver2.top()) return 1;
			if(rev_stk_ver1.top() < rev_stk_ver2.top()) return -1;
			rev_stk_ver1.pop();
			rev_stk_ver2.pop();
	    }
	    while(!rev_stk_ver1.empty())
	    {
	        if(rev_stk_ver1.top() != 0) return 1;
			rev_stk_ver1.pop();	
	    }
	    while(!rev_stk_ver2.empty())
	    {
	    	if(rev_stk_ver2.top() != 0) return -1;
	    	rev_stk_ver2.pop(); 
	    }
	    return 0;
    }
};
