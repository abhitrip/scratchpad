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
    bool isPalindrome(ListNode* head) {
        if(!head) return true;
        ListNode *slow = head,*fast = head->next;
        while(fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        // Now reverse second half of listo
        ListNode *curr = slow->next;
        slow->next = nullptr;
        ListNode *prev = nullptr,*next = nullptr;
        while(curr)
        {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        
        
        while(prev && head )
        {
           
            if(prev->val!=head->val) return false;
            prev=prev->next;head=head->next;
        }
        
        return true;
        
        
    }
};