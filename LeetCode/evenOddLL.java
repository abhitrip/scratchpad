class ListNode{
    int val;
    ListNode next;
    ListNode(int x){val=x;next=null;}
}
public class evenOddLL {
    ListNode head;
    public evenOddLL(){

        head = new ListNode(1);
        head.next = new ListNode(2);

        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        head.next.next.next.next.next = new ListNode(6);

    }
    public ListNode gethead(){
        return head;
    }
    public void traverse(ListNode node)
    {
        ListNode curr = head;
        while(curr!=null)
        {
            System.out.println(curr.val);
            curr=curr.next;
        }
    }
    public ListNode oddEvenList(ListNode head){

        ListNode odd = head;
        ListNode oddref = odd;
        if(odd==null)
            return odd;
        ListNode even = head.next;
        if((even==null))
            return odd; // return head;
        ListNode evenHead = new ListNode(0);
        ListNode refevenHead = evenHead;
        ListNode prev=null;
        while((odd!=null)&&(odd.next!=null)){
            evenHead.next = odd.next;
            prev = odd;
            odd.next = odd.next.next;


            evenHead.next.next = null;
            evenHead = evenHead.next;
            odd = odd.next;

        }
        if(odd!=null)
            odd.next = refevenHead.next;
        else
            prev.next = refevenHead.next;
       return oddref;

    }
    public ListNode reverseBetween(ListNode head,int m,int n){
        if(head==null)
            return head;
        int i=1;
        ListNode retHead = head;
        ListNode lastHeadBeforeRev = head;
        while(i<m-1)
        {
            lastHeadBeforeRev = lastHeadBeforeRev.next;
            i++;
        }
        ListNode curr=null,currRef=null,next=null;
        ListNode prev = null;
        if(m!=1){
        curr = lastHeadBeforeRev.next;
        currRef = curr;
        lastHeadBeforeRev.next=null;
        }

        if(m==1)
        {
            curr = lastHeadBeforeRev;
            currRef = curr;
        }
        while(i<n)
        {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
            i++;
        }
        if(m==1)
        {
            lastHeadBeforeRev.next=null;
        }
        currRef.next = next;
        lastHeadBeforeRev.next = prev;
        //prev.next = next;
        return retHead;
    }

    public static void main(String[] args){
        evenOddLL obj = new evenOddLL();
        ListNode hd = obj.gethead();
        // obj.traverse(hd);
        // ListNode oe = obj.oddEvenList(hd);
        ListNode rl = obj.reverseBetween(hd,1,4);
        obj.traverse(rl);
    }
}
