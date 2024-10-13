# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head.next

        curVal = 0
        while b:
            while b.val != 0:
                curVal += b.val
                b = b.next
            tmp = ListNode(curVal, b)
            curVal = 0
            a.next = tmp
            a = b
            b = b.next

        dummyHead = ListNode(-1, head)

        a = dummyHead

        while a:
            if a.next.val == 0:
                a.next = a.next.next
            
            a = a.next

        return dummyHead.next