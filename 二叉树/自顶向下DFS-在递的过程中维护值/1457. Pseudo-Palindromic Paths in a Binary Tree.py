from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        cnt = defaultdict(int)

        odd_cnt = 0
        ans = 0

        def dfs(root):
            nonlocal ans

            if not root:
                return
            
            if not root.left and not root.right:
                odd_cnt = 0
                for k, v in cnt.items():
                    if v % 2 == 1:
                        odd_cnt += 1
                        if odd_cnt > 1:
                            break
                if odd_cnt <= 1:
                    ans += 1
                    return
            
            if root.left:
                cnt[root.left.val] += 1
                dfs(root.left)
                cnt[root.left.val] -= 1
            
            if root.right:
                cnt[root.right.val] -= 1
                dfs(root.right)
                cnt[root.right.val] -= 1

        cnt[root.val] += 1
        dfs(root)

        return ans