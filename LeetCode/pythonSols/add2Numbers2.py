# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Non Rec solution
        stk1=[]
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        stk2=[]
        while l2:
            stk2.append(l2.val)
            l2 = l2.next


        prev = None
        s,c=0,0
        while stk1 or stk2:
            s=c
            if stk1:
                s+=stk1.pop()
            if stk2:
                s+=stk2.pop()
            node = ListNode(s%10)
            c = s/10
            node.next = prev
            prev = node
        if c:
            node = ListNode(c)
            node.next = prev
            return node
        return prev

    def addTwoNumbersRecs(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getLength(l):
            n=0
            while l:
                l=l.next
                n+=1
            return n

        def recursiveAdd(list1,list2,offset):
            if not list1: return None
            curr = ListNode(list1.val+list2.val) if offset==0 else ListNode(list1.val)
            next = recursiveAdd(list1.next,list2.next,0) if offset==0 else recursiveAdd(list1.next,list2,offset-1)
            if next and next.val>=10:
                next.val = next.val%10
                curr.val += 1

            curr.next = next
            return curr

        l1length = getLength(l1)
        l2length = getLength(l2)
        big,small = (l1,l2) if l1length>l2length else(l2,l1)
        resNode = ListNode(1)
        resNode.next = recursiveAdd(big,small,abs(l1length-l2length))
        if resNode.next.val>=10:
            resNode.next.val=resNode.next.val%10
            return resNode
        return resNode.next










