/*
Given an absolute path for a file (Unix-style), simplify it. 

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, 
so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, 
so it cancels out whatever the last directory was. For more information, 
look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
*/

#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    string simplifyPath(string path) {
         vector<string> stk;
         int last_pos = 0;
         int pos = 0;
         int len=length(path);
         while(-1!=(pos=temp_path.find("/"))
         {
             len = length(temp_path);
             if(pos<len-1)
             {
                 if(path[pos+1]==".")
                 {
                     if(pos<len-2 && path[pos+2]==".")
                     {
                         if(!stk.empty())
                         {
                             stk.pop_back();
                         }
                     }
                 }
             }
             else
             {
                string  sub_path = string(path,last_pos+1,pos);
                stk.push_back(sub_path);
             }
             last_pos=pos;
             temp_path.replace(pos,1,"#");
         }
         if(last_pos<len-1)
         {
             string sub_path = string(temp_path,last_pos);
             stk.push_back(sub_path);
         }
    }
};
