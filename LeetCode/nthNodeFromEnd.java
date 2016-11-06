/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode curr = head;
        ListNode adv = curr;
        ListNode prev = curr;
        int i=0;
        while(i<n)
        {
            prev = adv;
            adv=adv.next;
            i++;
        }

        if(adv==null)
            {

                return head.next;
            }
        while(adv!=null && adv.next!=null)
        {
            curr = curr.next;
            adv=adv.next;
        }

        System.out.println(curr.val);
        curr.next = curr.next.next;
        return head;


    }
}
