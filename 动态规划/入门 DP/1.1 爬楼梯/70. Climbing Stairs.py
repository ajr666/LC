from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def dfs(i):
            if i == 1:
                return 1
            if i == 2:
                return 2
            return dfs(i - 1) + dfs(i - 2)
        
        return dfs(n)
    


class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        f = [0 for _ in range(n + 1)]

        f[1] = 1
        f[2] = 2

        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n] 


