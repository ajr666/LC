# Definition for singly-linked list.
from math import gcd


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p.next:
            nd = ListNode(gcd(p.val, p.next.val), p.next)
            p.next = nd
            p = nd.next

        return head