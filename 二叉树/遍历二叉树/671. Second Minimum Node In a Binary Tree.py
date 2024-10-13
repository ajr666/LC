# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pre(self, root, res):
        if not root:
            return
        self.pre(root.right, res)
        res.append(root.val)
        self.pre(root.left, res)

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        res = []
        self.pre(root, res)

        res.sort()
        print(res)

        a = res[0]
        for i in range(0, len(res)):
            if res[i] != a:
                return res[i]
            
        return -1 

