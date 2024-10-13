class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pre(self, root, res):
        if not root:
            return
            
        if not root.left and not root.right:
            res.append(root.val)
            return
        
        self.pre(root.left, res)
        self.pre(root.right, res)

        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # a = b = []
        a = []
        b = []
        self.pre(root1, a)
        self.pre(root2, b)
        print(a, b)

        return a == b   