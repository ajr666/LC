from functools import cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i):
            if i == 0:
                return 1
            
            res = 0
            for j in range(0, n):
                if nums[j] <= i:
                    res += dfs(i - nums[j])

            return res

        return dfs(target)
    

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        f = [0 for _ in range(target + 1)]

        f[0] = 1

        for i in range(1, target + 1):
            for j in range(0, n):
                if i >= nums[j]:
                    f[i] += f[i - nums[j]]

        return f[target]