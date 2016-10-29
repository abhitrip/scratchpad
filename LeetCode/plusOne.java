/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int recAdd(ListNode head)
    {
        if(head==null)
            return 0;
        if(head.next==null)
        {
            int sum = head.val+1;
            int carry = 0;
            carry = sum/10;
            sum=sum%10;
            head.val = sum;
            return carry;
            
        }
        int carry = recAdd(head.next);
        int sum = head.val + carry;
        carry = sum/10;
        sum = sum%10;
        head.val = sum;
        return carry;
        
    }
    public ListNode plusOne(ListNode head) {
        if(head==null)
            return head;
        int carry = recAdd(head);
        if(carry==1)
            {
                ListNode newhead = new ListNode(1);
                newhead.next = head;
                return newhead;
            }
        
        return head;
    }
}