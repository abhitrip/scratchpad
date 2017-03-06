/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    typedef struct ListNode listnode;
    if(head==NULL)  return head;
    listnode *prev = NULL;
    listnode *curr = head;
    listnode *next = NULL;
    while(curr!=NULL)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    
    return prev;
    
    
    
}