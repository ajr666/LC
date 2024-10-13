# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 什么时候需要dummyHead? 需要删除头节点的时候
        dummyHead = ListNode(-1, head)
        p = dummyHead

        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return dummyHead.next