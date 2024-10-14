class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        n = len(time)
        l, r = 0, totalTrips * min(time)

        def check(mid):
            nonlocal n, totalTrips
            res = 0
            for i in range(n):
                res += mid // time[i]

            return res >= totalTrips

        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid 
            else:
                l = mid + 1

        return l