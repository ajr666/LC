from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0 for _ in range(n + 1)]

        f[0] = 0
        f[1] = nums[0]

        for i in range(2, n + 1):
            f[i] = max(f[i - 1], f[i - 2] + nums[i - 1])

        return f[n]
    

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i):
            if i < 0:
                return 0
            return max(dfs(i - 1), dfs(i - 2) + nums[i])
        
        return dfs(n - 1)