# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0

        # traverse the tree and keeping the parent and grandparent
        def dfs(root, p, gp):
            nonlocal ans

            if not root:
                return

            if gp and gp.val % 2 == 0:
                ans += root.val

            dfs(root.left, root, p)
            dfs(root.right, root, p)

        dfs(root, None, None)

        return ans