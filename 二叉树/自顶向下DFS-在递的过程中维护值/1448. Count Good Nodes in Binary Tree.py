# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from cmath import inf


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root, maxV): # maxV: the max value of the path root->parent 
            nonlocal ans
            
            if not root:
                return
            
            if root.val >= maxV:
                print(root.val)
                ans += 1
                maxV = root.val
            
            dfs(root.left, maxV)
            dfs(root.right, maxV)

        dfs(root, -inf)

        return ans