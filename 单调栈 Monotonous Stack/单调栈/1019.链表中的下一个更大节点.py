# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        p = head
        n = 0
        nums = []
        while p:
            nums.append(p.val)
            n += 1
            p = p.next

        ans = [0 for _ in range(n)]

        st = []

        for i, num in enumerate(nums):
            if not st or nums[st[-1]] >= num:
                st.append(i)
            else:
                while st and nums[st[-1]] < num:
                    idx = st.pop()
                    ans[idx] = num
                st.append(i)

        return ans




        