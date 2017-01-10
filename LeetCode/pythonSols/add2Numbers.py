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
        s,c=0,0
        res = ListNode(0)
        head = res
        while l1 or l2:
            s = l1.val+l2.val if l1 and l2 else (l1 or l2).val
            s += c
            c = s/10
            s = s%10
            res.next = ListNode(s)
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if c:
            res.next = ListNode(c)

        return head.next
