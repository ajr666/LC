class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # if max(dist) > hour:
        #     return -1

        n = len(dist)

        l, r = 1, 1_000_000_000

        def check(mid):
            nonlocal hour, n
            res = 0
            for i in range(n - 1):
                res += math.ceil(dist[i] / mid)
            res += dist[-1] / mid
            return res <= hour

        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        
        print(l)

        if check(l):
            return l
        
        return -1
