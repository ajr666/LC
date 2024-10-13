# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def judge(a, b): # judge 2 subTree 
            if not a or not b:
                return a == b
            if a.val != b.val:
                return False
            return judge(a.left, b.right) and judge(a.right, b.left)
        
        return judge(root.left, root.right)