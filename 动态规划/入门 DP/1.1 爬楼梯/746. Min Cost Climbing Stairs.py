from functools import cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def dfs(i):
            if i == 0:
                return 0
            if i == 1:
                return 0
            if i == 2:
                return min(cost[0], cost[1])
            
            return min(dfs(i - 1) + cost[i - 1], 
                       dfs(i - 2) + cost[i - 2])
        
        return dfs(n)
    

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       n = len(cost)
       f = [0 for _ in range(n + 1)]
       f[0] = 0
       f[1] = 0
       for i in range(2, n + 1):
           f[i] = min(f[i - 1] + cost[i - 1], f[i - 2] + cost[i - 2])

       return f[n]

       