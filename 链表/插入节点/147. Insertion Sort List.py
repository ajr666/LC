# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def deleteNode(p): # delete p.next
            t = p.next
            p.next = p.next.next
            return t
        
        def insertNode(q, t): # insert t between q and q.next
            t.next = q.next.next
            q.next = t

        dummyHead = ListNode(-1, head)
        p = dummyHead

        while p.next:
            t = deleteNode(p)

            q = dummyHead
            while q.next != t and q.next.val < t.val:
                q = q.next

            insertNode(q, t)

            p = p.next

        return dummyHead.next