from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque()

        ans = []

        q.append(root)

        while q:
            size = len(q)
            for i in range(size):
                t = q.popleft()
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
                if i == size - 1:
                    ans.append(t.val)

        return ans
    

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        maxLev = 0

        def dfs(root, lev):
            nonlocal maxLev

            if not root:
                return
            
            if lev > maxLev:
                maxLev = lev
                ans.append(root.val)

            dfs(root.right, lev + 1)
            dfs(root.left, lev + 1)

        dfs(root, 1)

        return ans