#Definition for singly-linked list.
import collections
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        nodeQ = collections.deque()
        refHead = head
        while refHead:
            nodeQ.append(refHead)
            refHead=refHead.next
        prev,refHead = None,None

        while nodeQ:

            front= nodeQ.popleft()
            rear = nodeQ.pop() if nodeQ else None
            front.next = rear
            if rear:
                rear.next = None
            if prev:
                prev.next = front
            prev = rear
            if rear==None:
                break




if __name__=="__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    #node.next.next.next = ListNode(4)
    sol = Solution()
    sol.reorderList(node)
    while node:
        print node.val
        node = node.next

