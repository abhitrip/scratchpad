/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {

        if(lists.length<1)
            return null;

        PriorityQueue<ListNode> heapQ = new PriorityQueue<>(new Comparator<ListNode>(){
            @Override
            public int compare(ListNode l1,ListNode l2)
            {
                return l1.val-l2.val;
            }

        });
        for(ListNode kthlist:lists)
        {
            if(kthlist!=null)
                heapQ.add(kthlist);

        }

        // Now create Dumy Node
        ListNode res = new ListNode(0);
        ListNode head = res;
        while(!heapQ.isEmpty())
        {
            ListNode curr = heapQ.poll();
            res.next = curr;
            if(curr.next!=null)
                heapQ.offer(curr.next);
            res = res.next;
        }

        return head.next;
    }
}
