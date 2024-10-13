# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical = []

        a = head
        b = head.next
        a_idx = 0
        
        while b.next:
            if a.val < b.val and b.val > b.next.val:
                critical.append(a_idx + 1)
            if a.val > b.val and b.val < b.next.val:
                critical.append(a_idx + 1)
            
            b = b.next
            a = a.next
            a_idx += 1

        if len(critical) <= 1:
            return [-1, -1]
        
        minD = critical[1] - critical[0]
        maxD = critical[-1] - critical[0]

        for i in range(1, len(critical) - 1):
            minD = min(minD, critical[i + 1] - critical[i])

        return [minD, maxD] 