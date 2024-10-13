class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pre(self, root, res):
        if not root:
            return 
        if root.left and not root.left.left and not root.left.right:
            self.res += root.left.val
            print(self.res)

        self.pre(root.left, self.res)
        self.pre(root.right, self.res)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.pre(root, self.res)

        return self.res