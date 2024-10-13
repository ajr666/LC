# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-1, head)
        deleteV = 200
        
        p = dummyHead

        while p.next:
            if p.next.next and p.next.val == p.next.next.val:
                deleteV = p.next.val
            if p.next.val == deleteV:
                p.next = p.next.next
            else:
                p = p.next

        return dummyHead.next