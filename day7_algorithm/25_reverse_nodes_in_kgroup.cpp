//Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
//If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
//You may not alter the values in the nodes, only nodes itself may be changed.
//Only constant memory is allowed.

//For example,
//Given this linked list: 1->2->3->4->5
//For k = 2, you should return: 2->1->4->3->5
//For k = 3, you should return: 3->2->1->4->5

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
class Solution {
public:
	ListNode* reverseList(ListNode* head, int k)
	{
	    ListNode* cur_node  = head->next;
		ListNode* pre_node = head;
		while(k - 1 > 0 && cur_node != NULL)
		{
			pre_node->next = cur_node->next;
			cur_node->next = head;
			head = cur_node;
			cur_node = pre_node->next;
			k--;
		}
		return head;
	}
   
    ListNode* reverseKGroup(ListNode* head, int k) {
        int len = 0;
        ListNode* cur_node = head;
		while(cur_node != NULL)
		{
			len++;
			cur_node = cur_node->next;
		}
		if(k > len) return head;
		head = reverseList(head, k);
		len -= k;
		ListNode* pre_sub_head = head;

	    int cnt = 0;
	    while(cnt != k - 1 && pre_sub_head->next != NULL)
	    {
	        pre_sub_head = pre_sub_head->next;
	        cnt++;
	    }
	    ListNode* sub_head = pre_sub_head->next;
	    
	    while(sub_head != NULL)
	    {
	    	if(k > len) break;
	        sub_head = reverseList(sub_head, k);
	        len -= k;
	        pre_sub_head->next = sub_head;
	        pre_sub_head = sub_head;
	        cnt = 0;
	        while(cnt != k - 1 && pre_sub_head->next != NULL)
	        {
	            pre_sub_head = pre_sub_head->next;
	            cnt++;
	        }
	        sub_head = pre_sub_head->next;
	    }
		return head;
    }
};
