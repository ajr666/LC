# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# every part has N/k elements, except the first N%k parts have an extra one.
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        p = head

        while p:
            n += 1
            p = p.next

        ans = []

        if k > n:
            p = head
            while p:
                t = p.next
                p.next = None
                ans.append(p)
                p = t
            
            for _ in range(k-n):
                ans.append(None)
            
            return ans
        
        length = n // k
        a = b = head
        m = n % k

        for _ in range(m):
            for _ in range(length):
                b = b.next
            t = a
            a = b.next
            b.next = None
            b = a
            ans.append(t)

        while b:
            for _ in range(length - 1):
                b = b.next
            t = a
            a = b.next
            b.next = None
            b = a
            ans.append(t)

        return ans