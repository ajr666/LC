# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root):
        if not root:
            return
        
        if not root.left and not root.right:
            res = 0
            for n in self.path:
                res = res * 10 + n
            self.ans += res
            return
        
        # for each child nodes:
        # 1. dfs
        # 2. backtrack
        if root.left:
            self.path.append(root.left.val)
            self.dfs(root.left)
            self.path.pop()
        if root.right:
            self.path.append(root.right.val)
            self.dfs(root.right)
            self.path.pop()

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.path = [root.val] # first process root node

        self.dfs(root) # the proceess child nodes of root node

        return self.ans