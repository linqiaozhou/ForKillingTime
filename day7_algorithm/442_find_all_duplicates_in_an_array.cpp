/*Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]*/
#include"common.hpp"
 
class Solution {
public:
	void swap(int& a, int& b)
   	{
   	    int temp = a;
    	a = b;
   		b = temp;
   	}
    vector<int> findDuplicates(vector<int>& nums) {
        int len = nums.size();
	   	int pos = 0;
	   	while(pos < len)
	   	{
	   		if(nums[pos]> 0 && nums[pos] < len+1 
			   && nums[pos] != pos + 1 && nums[pos]!= nums[nums[pos]-1])
			{
	    	    swap(nums[pos],nums[nums[pos]-1]);
	   		}
	   		else
	   		{
	   			++pos;
    		}
	    }
	    vector<int> ret;
	    for(int i = 0; i < len; i++)
	   	{
	   		if(nums[i] != i + 1)
	   		{
	   		    ret.push_back(nums[i]);
    		}
		}
	   	return ret;
    }
};
