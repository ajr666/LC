from collections import Counter
from functools import cache

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt.keys())

        @cache
        def dfs(i):
            if i < 0:
                return 0

            j = i - 1
            while j >= 0 and a[j] > a[i] - 2:
                j -= 1

            return max(dfs(i - 1),
                       cnt[a[i]] * a[i] + dfs(j))
        
        return dfs(len(a) - 1)
    

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt.keys())
        n = len(a)

        f = [0 for _ in range(n)]

        f[0] = a[0] * cnt[a[0]]

        for i in range(1, n):
            j = i - 1
            while j >= 0 and a[j] >= a[i] - 2:
                j -= 1

            f[i] = max(f[i - 1], f[j] + a[i] * cnt[a[i]])

        return f[n - 1]