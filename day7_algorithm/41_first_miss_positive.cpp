//First Missing Positive
//Given an unsorted integer array, find the first missing positive integer.
//For example,
//Given [1,2,0] return 3,
//and [3,4,-1,1] return 2.
//Your algorithm should run in O(n) time and uses constant space.

#include"common.hpp"

class Solution {
    public:
    	void swap(int& a, int& b)
    	{
    		int temp = a;
    		a = b;
    		b = temp;
    	}
	    int firstMissingPositive(vector<int>& nums)
	    {
	    	int len = nums.size();
	    	if(len<1) return 1;
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
	    	for(int i = 0; i < len; i++)
	    	{
	    		if(nums[i] != i + 1)
	    		{
	    			return i+1;
	    		}
	    	}
	    	return len+1;
	    }
};
