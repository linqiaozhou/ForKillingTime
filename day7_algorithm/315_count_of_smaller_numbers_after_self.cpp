/*You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
Example:
Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.*/

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int len = nums.size();
        vector<int> ret; 
        if(len == 0) return ret;
        for(int i = 0; i < len; i++)
        {
            int cnt = 0;
            for(int j = i + 1; j < len; j++)
            {
                if(nums[j] < nums[i])
                {
                    cnt++;
                }
            }
            ret.push_back(cnt);
        }
        
        return ret;
    }
};
