# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pre(self, root, d):
        if not root:
            return
        if not root.left and not root.right:
            self.ans = min(self.ans, d + 1)
            return
        
        self.pre(root.left, d + 1)
        self.pre(root.right, d + 1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 1e5 + 10
        self.pre(root, 0)
        return self.ans