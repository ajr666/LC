# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        st = set(nums)
        ans = 0

        inNum = False

        p = head

        while p:
            if not inNum:
                if p.val in st:
                    inNum = True
                    ans += 1
                else:
                    pass
            elif inNum:
                if p.val in st:
                    pass
                else:
                    inNum = False
            
            p = p.next

        return ans
            